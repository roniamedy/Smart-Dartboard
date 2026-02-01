# 🎯 Smart Dartboard

A DIY attempt to build an automated dart scoring system using Computer Vision. 

## Project Status: Work in Progress

This is my first deep dive into **Python** and **Computer Vision**. The goal is to build a software that detects darts on a board and calculates the score automatically.

I am focusing on writing clean code and understanding the math behind image processing (Matrices, Perspective Warping).

## Target Hardware

This project is currently **under development** and is intended to work with standard **3-camera setups**, as commonly used in the DIY dart community.

## 📂 Project Structure
```text
Smart Dartboard/
│
├── modules/
│   ├── game_engine/
│   └── vision_manager/ 
│       ├── camera.py
│       ├── processor.py   
│       └── vision_manager.py 
│
├── .gitignore     
├── main.py      
└── README.md      