__author__ = 'kkboy'
import os, sys, inspect, thread, time
# bad import lib way
# do not use it in app
# use it in practice
from x64 import Leap
from x64.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):

    # The Controller object is initialized
    def on_init(self, controller):
        print "Device initialized"

    # The Controller has connected to the Leap Motion service/daemon
    def on_service_connect(self, controller):
        print "service connected"

    # The status of a Leap Motion hardware device changes
    def on_device_change(self, controller):
        print "Device_change"

    # The application has gained operating system input focus and will start receiving tracking data
    def on_focus_gained(self, controller):
        print "Focus gain"

    # The application has lost operating system input focus
    # The application will stop receiving tracking data unless it has set the BACKGROUND_FRAMES_POLICY
    def on_focus_lost(self, controller):
        print "Focus lost"

    # The Controller connects to the Leap Motion service/daemon and the Leap Motion hardware is attached.
    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
        controller.set_policy(Leap.Controller.POLICY_IMAGES)
        controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)

    # A new Frame of tracking data is available
    def on_frame(self, controller):
        # controller is a Leap.Controller object
        if controller.is_connected:
            # The latest frame
            frame = controller.frame()
            # The previous frame
            # previous = controller.frame(1)
            print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
                frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

    # The Controller has lost its connection to the Leap Motion service/daemon
    def on_service_disconnect(self, controller):
        print "service disconnected"

    # The Controller disconnects from the Leap Motion service/daemon or the Leap Motion hardware is removed
    def on_disconnect(self, controller):
        print "Device disconnected"

    # The Controller object is destroyed
    def on_exit(self, controller):
        print "Exit"


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()