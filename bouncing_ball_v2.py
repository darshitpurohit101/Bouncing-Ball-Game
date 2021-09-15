# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:44:08 2021

@author: DARSHIT PUROHIT
"""

import cv2
import numpy as np

def play_area():

    window = np.zeros((520,680), dtype='uint8') # creating window
    
    #defining the borders
    top = int(0.05 * window.shape[0])
    left = int(0.05 * window.shape[1])
    right = left
    img = cv2.copyMakeBorder(window,top, 0, left, right, cv2.BORDER_CONSTANT, None, (130,255,255) )
    cv2.putText(img, "BOUNCING BALL", (150,150) , cv2.FONT_HERSHEY_SIMPLEX , 2, (125,255,255), 2)
    cv2.putText(img, "How to play?", (150,230) , cv2.FONT_HERSHEY_PLAIN , 2, (125,255,255), 2)
    cv2.putText(img, "> Move your mouse left/right to control the racket", (150,260) , cv2.FONT_HERSHEY_PLAIN , 1, (125,255,255), 1)
    cv2.putText(img, "> Don't let the BALL FALL ", (150,290) , cv2.FONT_HERSHEY_PLAIN , 1, (125,255,255), 1)
    cv2.putText(img, "Press 'P' to start", (255,500), cv2.FONT_HERSHEY_PLAIN , 2, (125,255,255))
    cv2.imshow('a',img)
    if cv2.waitKey(0) == ord('p'):
        
        #for the ballanimation
        dx,dy = 5, 5
        bx,by=100,200
        
        def move_racket(event, x, y, flags, para):
            nonlocal img, r1x, r2x
            r1x, r2x, r1y, r2y =0,80,520,540
            imgCopy = img.copy()
    
            if event==cv2.EVENT_MOUSEMOVE:
                r1x += x
                r2x += x
                
                #Handling racket scroll
                if r1x<35:
                    r1x=35
                    r2x=114
                elif r2x>643:
                    r2x=711
                    r1x=631
                
                cv2.rectangle(imgCopy, (r1x,520), (r2x,540), (130,255,255), -1)  #racket for the game [using +x to keep the width on the rect]
    
            cv2.imshow('a',imgCopy)
        r1x, r2x =298,378 #Intitial state of the racket
        while True:
            
            cv2.imshow('a',img)
            if cv2.waitKey(33) == 27: #ESC key
                break
        
            img = cv2.copyMakeBorder(window,top, 0, left, right, cv2.BORDER_CONSTANT, None, (130,255,255) )
            
            # Increment the position
            bx = bx+dx
            by = by+dy
            cv2.circle(img,(bx,by),10,(255,0,0),-1)
            cv2.rectangle(img, (r1x,520), (r2x,540), (130,255,255), -1)
            cv2.setMouseCallback('a', move_racket)
            
            #Changing the direction of the ball
            #Bounsing effect
            if r1x-10<=bx<=r2x+10 and 510<=by<=520: #Position of the racket
                dx *= -1
                dy *= -1
                bx+=1
                by-=2
            elif by<=50: #Top
                dy *= -1
                bx += 1
            elif bx<=53: #Left
                dx *= -1
            elif bx>=670: #Right
                dx*=-1
                dy+=1
            elif by>530:
                break
         
        # while True:    
        cv2.putText(img, "Game Over......", (150,230) , cv2.FONT_HERSHEY_PLAIN , 2, (125,255,255), 2)  
        cv2.putText(img, "Press ESC to end", (150,260) , cv2.FONT_HERSHEY_PLAIN , 1, (125,255,255), 1)
        cv2.putText(img, "Press 'R' to restart", (150,290) , cv2.FONT_HERSHEY_PLAIN , 1, (125,255,255), 1)
        cv2.imshow('a',img)
        k = cv2.waitKey(10000)
        if k == ord('r'):
            play_area()
        elif k == 27:
            cv2.destroyAllWindows()
            
            
        cv2.destroyAllWindows()

play_area()

