class SceneManager:
    def __init__(self, scenes, entry_scene):
        self.scenes = scenes
        self.scene_stack = [self.scenes[entry_scene]]

    def get_active_scene(self):
        return self.scene_stack[-1]

    def update(self):
        self.get_active_scene().update()

    def render(self, screen):
        self.get_active_scene().render(screen)

    def get_event(self, event):
        self.get_active_scene().get_event(event)