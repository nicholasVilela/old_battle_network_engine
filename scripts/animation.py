from resources import resources


class Animation:
    def __init__(self, name, frame_count, frame_duration, loop=False, playing=False):
        self.name = name

        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.frame = 0
        self.frame_timer = 0

        self.loop = loop
        self.finished = False

        self.playing = playing

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

                if self.loop:
                    self.play()