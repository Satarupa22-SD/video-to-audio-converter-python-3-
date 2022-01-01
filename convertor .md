```python
pip install moviepy
```

    Requirement already satisfied: moviepy in c:\users\lucy22\anaconda3\lib\site-packages (1.0.3)
    Requirement already satisfied: decorator<5.0,>=4.0.2 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (4.4.2)
    Requirement already satisfied: proglog<=1.0.0 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (0.1.9)
    Requirement already satisfied: tqdm<5.0,>=4.11.2 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (4.59.0)
    Requirement already satisfied: numpy>=1.17.3 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (1.20.1)
    Requirement already satisfied: imageio<3.0,>=2.5 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (2.9.0)
    Requirement already satisfied: requests<3.0,>=2.8.1 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (2.25.1)
    Note: you may need to restart the kernel to use updated packages.
    Requirement already satisfied: imageio-ffmpeg>=0.2.0 in c:\users\lucy22\anaconda3\lib\site-packages (from moviepy) (0.4.5)
    Requirement already satisfied: pillow in c:\users\lucy22\anaconda3\lib\site-packages (from imageio<3.0,>=2.5->moviepy) (8.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\lucy22\anaconda3\lib\site-packages (from requests<3.0,>=2.8.1->moviepy) (2020.12.5)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\lucy22\anaconda3\lib\site-packages (from requests<3.0,>=2.8.1->moviepy) (1.26.4)
    Requirement already satisfied: chardet<5,>=3.0.2 in c:\users\lucy22\anaconda3\lib\site-packages (from requests<3.0,>=2.8.1->moviepy) (4.0.0)
    Requirement already satisfied: idna<3,>=2.5 in c:\users\lucy22\anaconda3\lib\site-packages (from requests<3.0,>=2.8.1->moviepy) (2.10)
    


```python
import moviepy.editor
```


```python
from tkinter.filedialog import *
```


```python
video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio
```


```python


audio.write_audiofile("sample.mp3")
print("Completed!")
```

    chunk:   1%|▍                                                             | 38/5015 [00:00<00:13, 378.47it/s, now=None]

    MoviePy - Writing audio in sample.mp3
    

                                                                                                                           

    MoviePy - Done.
    Completed!
    

    


```python

```
