import tkinter as tk
from PIL import ImageTk, Image
import cv2
# import face_recognition
from face_recognition_code import attendance
#  add a function from AIComputerVision-master folder from the file of person_counter.py

# string1="Counting/person_counter"
# from  string1 import personcounter
# from AIComputerVision-master.person_counter import person_counter

# Function to handle the Attendance button click event
def handle_attendance():
    # Remove the buttons and label
    # button1.place_forget()
    # button2.place_forget()
    # label.place_forget()
    class_name = input("Enter the class name: ")

    # Call the face recognition function
    attendance_taken=attendance(class_name)
    print(attendance_taken)

    # Create a listbox widget
    listbox = tk.Listbox(window)

    # Add the list of attendees to the listbox widget
    for attendee in attendance_taken:
        listbox.insert(tk.END, attendee)

    # Set the heading of the listbox widget
    # listbox.config(header_text="Attendees")

    # Place the listbox widget below the attendance button
    listbox.place(relx=0.4, rely=0.7, anchor=tk.CENTER)

    
    # Create a canvas to display the camera feed
    # canvas = tk.Canvas(window, width=800, height=600)
    # canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    # # Get a reference to webcam #0 (the default one)
    # video_capture = cv2.VideoCapture(0)

    # Function to update the canvas with the current frame
    def update_frame():
        _, frame = video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = ImageTk.PhotoImage(Image.fromarray(frame))
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image
        window.after(10, update_frame)  # Update every 10 milliseconds

    # Start updating the canvas with the webcam feed
    # update_frame()
    
    # Create a "Back" button
    # def go_back():
    #     # Remove the canvas and go back to the previous state
    #     canvas.place_forget()
    #     button1.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    #     button2.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
    #     label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # back_button = tk.Button(window, text="Back", font=("Arial", 14), padx=10, pady=5, command=go_back)
    # back_button.place(relx=0.05, rely=0.05, anchor=tk.NW)

# Create the main window
window = tk.Tk()
window.title("GUI Example")
window.geometry("800x600")

# Set the background image
background_image = Image.open(r"C:\Users\Waleed Ahmed Shahid\Downloads\Smart_Attendence_System\background_image.jpg")
background_image = background_image.resize((800, 600), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create two buttons
label = tk.Label(window, text="Computer Vision Project", font=("Arial", 30), fg="white", bg="black")
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button1 = tk.Button(window, text="Attendance", font=("Arial", 14), padx=10, pady=5, command=handle_attendance)
button1.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

button2 = tk.Button(window, text="Count", font=("Arial", 14), padx=10, pady=5)
button2.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

# Start the main event loop
window.mainloop()
