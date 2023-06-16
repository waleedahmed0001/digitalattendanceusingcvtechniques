            if cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) == 0 or cv2.waitKey(1) & 0xFF == ord('q'):
               print("Camera window closed. Exiting program...")
               camera_open = False