from resources import resources
from enums import InstructionStates
from instruction import Instruction


class Animation:
    def __init__(self, name, frame_count, frame_duration, loop=False, playing=False, instructions=[]):
        self.name = name

        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.frame = 0
        self.frame_timer = 0

        self.loop = loop
        self.finished = False

        self.playing = playing

        self.instructions = instructions

    def play(self):
        self.frame = 0
        self.finished = False
        self.playing = True

    def pause(self):
        self.playing = False

    def update(self):
        if not self.playing or self.frame_count == 1:
            return

        if self.finished and not self.loop:
            return

        self.frame_timer += resources['dt']
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            
            if self.frame < (self.frame_count - 1):
                self.frame += 1
            else:
                self.finished = True
                self.reset_instructions()

                if self.loop:
                    self.play()

        self.update_instructions()

    def reset_instructions(self):
        for instruction in self.instructions:
            instruction.reset()

        self.instructions = []

    def add_instruction(self, frame, function, params):
        instruction = Instruction(
            frame=frame,
            function=function,
            params=params,
        )

        self.instructions.append(instruction)

    def update_instructions(self): 
        for instruction in self.instructions:
            if instruction.state == InstructionStates.IDLE and self.frame == (instruction.frame - 1):
                instruction.run()
                instruction.state = InstructionStates.FINISHED

            