# Audio-Visual Perception of Omnidirectional Video for Virtual Reality Applications

In this repository, we are sharing our developed tools and captured user data that we hope will enable in creating more immersive virtual reality experiences. This repository is for open source codes and materials for the ICMEW 2020 paper: *Audio-Visual Perception of Omnidirectional Video for Virtual Reality Applications*

### Abstract

Ambisonics, which constructs a sound distribution over the full viewing sphere, improves immersive experience in omnidirectional video (ODV) by enabling observers to perceive the sound directions. Thus, human attention could be guided by audio and visual stimuli simultaneously. Numerous datasets have been proposed to investigate human visual attention by collecting eye fixations of observers navigating ODV with head-mounted displays (HMD). However, there is no such dataset analyzing the impact of audio information. In this paper, we establish a new audio-visual attention dataset for ODV with mute, mono, and ambisonics. The user behavior including visual attention corresponding to sound source locations, viewing navigation congruence between observers and fixations distributions in these three audio modalities is studied based on video and audio content. From our statistical analysis, we preliminarily found that, compared to only perceiving visual cues, perceiving visual cues with salient object sound (i.e., human voice, siren of ambulance) could draw more visual attention to the objects making sound and guide viewing behaviour when such objects are not in the current field of view. The more in-depth interactive effects between audio and visual cues in mute, mono and ambisonics still require further comprehensive study. The dataset and developed testbed in this initial work will be publicly available with the paper to foster future research on audio-visual attention for ODV.

### Downloads

[User data](https://www.dropbox.com/s/idimreoj6cuvysl/dataset_public.zip?dl=0)

[ODVs](https://www.dropbox.com/s/wdzjvfgkqn19sry/videos.zip?dl=0)

### Fixation and saliency map estimation

Open-sourced script developed within visual attention estimation works for ODVs. The generated

#### Requirements

**Install using pip**

````bash
cd code/
virtualenv audio_visual
source activate audio_visual/bin/activate
pip3 install -r requirements.txt
````

#### Run

````bash
python3 fixmap2salmap.py -i dataset_public/ -o videos/ -r 100x200 -s True
````

*Parameters*
> -i: input user-data folder downloaded from [User data]
> -o: input ODV dataset downloaded from [ODVs]
> -r: required resolution output for saliency and fixation maps
> -s: flag for saliency output, default is False.

### Citation

| Paper accepted in [IEEE International Conference on Multimedia and Expo Workshops 2020 (ICMEW 2020)](https://www.2020.ieeeicme.org/) |
| ![qomex logo](img/logo.png) |

Please cite our [paper](https://github.com/cozcinar/omniAttention/blob/master/ICMEW2020.pdf) in your publications if it helps your research:

````
@inproceedings{icmew2020,
title = {audio-visual perception of omnidirectional video for virtual reality applications},
author = {Chao, F. and Ozcinar, C. and Wang, C. and Zerman, E. and Zhang, L. and Hamidouche, W. and Deforges, O. and Smolic, A.},
year = {2020},
date = {2020-10-28},
booktitle = {IEEE International Conference on Multimedia & Expo Workshops (ICMEW)},
tppubtype = {inproceedings}
}
````

### Contact

If you have any question, send an e-mail at [cagriozcinar@gmail.com]()
