# References

https://flyingframes.readthedocs.io/en/v0.11.0/carnot.html


----------------------------------
On Matt's laptop

docker run -it --name my-manim-container -v "/home/bellis/siena-manim:/manim/siena-manim" manimcommunity/manim /bin/bash

manim -p -ql text.py Text

manim -p -ql shapes.py Shapes


##### 

# Once in the docker environment
cd siena-manim

manim -p -ql word-problems.py SienaIntro
