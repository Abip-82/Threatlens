# Threatlens v2.0

Threatlens is an educational cybersecurity webapp desgined to serve as a beginner toolkit. It contains features like suspicious links analyzer, cipher encoder and decoder with user input key in current version. I plan to update and expand threatlens on iterations, adding new layers and features on each iteration like hashes generator, port scanner, password strength checker, and much more.

Why did I build Threatlens?
I am deeply interested in cybersecurity and programming in general. I wanted to build a security tool for a long time but did not have enough experience in building complex tools. Also, I noticed how most people are aware of phishing but still slip and fall into the trap all the time. So I wanted to start building and contribute. Hence, came up with the idea of Threatlens, a cybsersecurity toolkit for beginners. So, I built it!

What Threatlens does?
In the current version, Threatlens provides phishing link analyser and cipher encoder & decoder. In phishing link analyser, user can input suspicious links which undergoes the analysis logic and returns verdict, risk score as well reasons for that certain risk score. In cipher encoder/decoder users can enter plain texts/ encrypted texts along with their "secret key" and get results which is an encrypted text or decoded message.

These are the current features provided by Threatlens to help users and serve as an educational toolkit for cybersecurity learners to visualize and understand concepts. However, I plan to implement many other features like password strength checker, hash generator, port scanner, etc in upcomming versions (v3.0 and higher).

How it all fits together?
I used python for backend and js+css+html for frontend. The frontend sends the user entered URL in the form of JSON data, which then undergoes analysis. The core logic gets executed (different for different features) and returns the result back to the frontend in the form of JSON data. Then, it is displayed to the user.

Improvements from previous version:
1) Improved link analyser logic.
2) Fixed link analyser bug that flagged initial "/" from "https://" for redirection trap.
3) Added a dashboard for the site.
4) New cipher encoder/decoder feature with user input key.
5) UI improvements (like added the binary stream flow in the right side).

Built by Abip Mahat || Cybersecurity and Programming Enthusiast.


Evolution of ThreatLens
| Initial Prototype | Final Dashboard |
|---|---|
| ![V0.1](assets/initial_design.png) | ![V1.0](assets/final_Design.png) |e 

LINK TO THE WEBAPP:
https://threatlens-iota.vercel.app/
