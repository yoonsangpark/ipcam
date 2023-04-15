import os, platform
import vlc

class ooPlayer:
    def __init__(self, *args):
        if args:
            instance = vlc.Instance(*args)
            self.media = instance.media_player_new()
        else:
            self.media = vlc.MediaPlayer()

    def set_uri(self, uri):
        self.media.set_mrl(uri)

    def play(self, path=None):
        if path:
            self.set_uri(path)
            return self.media.play()
        else:
            return self.media.play()

    def pause(self):
        self.media.pause()

    def resume(self):
        self.media.set_pause(0)

    def stop(self):
        self.media.stop()

    def release(self):
        return self.media.release()

    def is_playing(self):
        return self.media.is_playing()

    def get_time(self):
        return self.media.get_time()

    def set_time(self, ms):
        return self.media.get_time()

    def get_length(self):
        return self.media.get_length()

    def get_volume(self):
        return self.media.audio_get_volume()

    def set_volume(self, volume):
        return self.media.audio_set_volume(volume)

    def get_state(self):
        state = self.media.get_state()
        if state == vlc.State.Playing:
            return 1
        elif state == vlc.State.Paused:
            return 0
        else:
            return -1

    def get_position(self):
        return self.media.get_position()

    def set_position(self, float_val):
        return self.media.set_position(float_val)

    def get_rate(self):
        return self.media.get_rate()

    def set_rate(self, rate):
        return self.media.set_rate(rate)

    def set_ratio(self, ratio):
        self.media.video_set_scale(0)
        self.media.video_set_aspect_ratio(ratio)

    def set_window(self, wm_id):
        if platform.system() == 'Windows':
            self.media.set_hwnd(wm_id)
        else:
            self.media.set_xwindow(wm_id)

    def add_callback(self, event_type, callback):
        self.media.event_manager().event_attach(event_type, callback)

    def remove_callback(self, event_type, callback):
        self.media.event_manager().event_detach(event_type, callback)

