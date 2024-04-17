import sys
import gi
from threading import Thread
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib
import cv2
import numpy

Gst.init(None)


image_arr = None

def gst_to_opencv(sample):
    buf = sample.get_buffer()
    caps = sample.get_caps()
    print(caps.get_structure(0).get_value('format'))
    print(caps.get_structure(0).get_value('height'))
    print(caps.get_structure(0).get_value('width'))

    print(buf.get_size())

    arr = numpy.ndarray(
        (caps.get_structure(0).get_value('height'),
         caps.get_structure(0).get_value('width'),
         3),
        buffer=buf.extract_dup(0, buf.get_size()),
        dtype=numpy.uint8)
    return arr

def new_buffer(sink, data):
    global image_arr
    sample = sink.emit("pull-sample")
    # buf = sample.get_buffer()
    # print "Timestamp: ", buf.pts
    arr = gst_to_opencv(sample)
    
    image_arr = arr
    
    return Gst.FlowReturn.OK


# main_loop = GLib.MainLoop()
# main_loop_thread = Thread(target=main_loop.run)
# main_loop_thread.start()

pipeline = Gst.parse_launch("\
    videotestsrc \
    ! video/x-raw,width=640,height=480,format=(string)BGR \
    ! appsink name=sink emit-signals=True")

sink = pipeline.get_by_name("sink")
sink.connect("new-sample", new_buffer, sink)


pipeline.set_state(Gst.State.PLAYING)
bus = pipeline.get_bus()

try:
    while True:
        message = bus.timed_pop_filtered(10000, Gst.MessageType.ANY)

        if image_arr is not None:
            cv2.imshow("appsink image arr", image_arr)
            cv2.waitKey(1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
