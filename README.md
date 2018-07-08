# GCD-Pattern-21B
An Interesting GCD problem from Harvard Math 21B. If you wish to see the question then visit 5.(c) qurstion in the below pdf
https://sites.fas.harvard.edu/~math21b/handouts/hw06.pdf

![alt text](https://github.com/GeVic/GCD-Pattern-21B/blob/master/gcd.png)

(To inccrease the size of the image you could change the ```dim``` value in the ```gcd.py```)

So, In order to explain this pattern I plotted the GCD(x,y) with coressponding pixel densities.
And it could be seen that the line patterns are drawn as a result. 

Also, the line pattern matches the equation ax = by. Which is very obvious as the 
Euclidean Algorithm for finding GCD(A,B) could be written as A = B.Q + R and if R = 0 then B = GCD(A,B).
And since A = B.Q + R represent line equation y = m.x + c, which in turn is y = mx if c = 0.

Thus, the lines in the above depiction corresponds to ax = by for intergral(a,b) and hence explains the line pattern.
Same could be seen with the plot below.

![alt text](https://github.com/GeVic/GCD-Pattern-21B/blob/master/line.png)

Now, the above line pattern is very similar to the GCD(a,b) pattern but not the same. This implies that this is the one of the possible way 
of solving GCD(a, b). Although this approch being slow as compares to Euclidean approach, it doesn't give us much of 
a solution.

## Why I did this?
The problem seems intresting. But still I think my explanation lacks something. It would be great if you wanna discuss 
the same.

## How can i edit the README..md file for better explanation?
Simple, create a pull request and I would love to hear your explanation. 
