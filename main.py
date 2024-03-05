#Import the moviepy library
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip


# Define a class for video clips
class VideoClip:
    # Class constructor
    def __init__(self, file_name, start_time, end_time):
        # Initialize the attributes
        self.file_name = file_name  # The name of the video file
        self.start_time = start_time  # The start time of the clip in seconds
        self.end_time = end_time  # The end time of the clip in seconds
        self.clip = VideoFileClip(file_name).subclip(start_time, end_time)  # The moviepy object for the clip

    # Define a method to show the clip
    def show(self):
        # Play the clip
        self.clip.preview()

    # Define a method to save the clip
    def save(self, output_file):
        # Write the clip to a file
        self.clip.write_videofile(output_file)


# Define a subclass for concatenated video clips
class ConcatenatedVideoClip(VideoClip):
    # Class constructor
    def __init__(self, clips, audio):
        # Call the superclass constructor with the first clip's file name and start time, and the last clip's end time
        super().__init__(clips[0].file_name, clips[0].start_time, clips[-1].end_time)
        # Concatenate all clips
        self.clip = concatenate_videoclips([clip.clip for clip in clips])
        # Add audio
        self.clip.audio = CompositeAudioClip([audio])

    # Override the save method to add "_combined" to the output file name
    def save(self, output_file):
        # Add "_combined" to the output file name
        output_file = output_file[:-4] + "_combined" + output_file[-4:]
        # Call the superclass save method
        super().save(output_file)


# Create an instance of VideoClip class
clip1 = VideoClip("one.mp4", 10, 15)
clip2 = VideoClip("two.mp4", 0, 3)
clip3 = VideoClip("one.mp4", 10, 15)

# Create an instance of AudioFileClip class
audio = AudioFileClip("audio.mp4")

# Create an instance of ConcatenatedVideoClip class
combined = ConcatenatedVideoClip([clip1, clip2, clip3], audio)

# Save the concatenated video clip
combined.save("output.mp4")