import tkinter as tk
from tkinter import messagebox
import os
import pygame
from pathlib import Path
from PIL import Image, ImageTk  

projectpath = Path(__file__).parent.parent.parent.resolve()

PRE_EXISTING_SAMPLES_DIR = projectpath / "tau_workshop"/ "app" / "samples"


def generate_samples(duration):
    # Simulate sample creation
    output_dir = f"{projectpath}/sashimi/uncond-2-layers"
    os.chdir(projectpath)
    os.system(
        f"python -m generate" \
        f" experiment=audio/sashimi-youtubebigband-ablate-2-layers" \
        f" checkpoint_path={projectpath}/checkpoints/sashimi_bigband_2l.pt" \
        f" n_samples=30" \
        f" l_sample={duration * 16000}" \
        f" load_data=false" \
        f" save_dir={output_dir}" \
        f" temp=1.0"          
    )
    return output_dir

# Function to list and play pre-existing samples
def show_existing_samples():
    def play_sample(filepath):
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    # Clear the dynamic content area
    clear_dynamic_content()

    tk.Label(dynamic_frame, text="Check out our band's greatest hits!").pack()

    # List sound files in the directory
    if not os.path.exists(PRE_EXISTING_SAMPLES_DIR) or not os.listdir(PRE_EXISTING_SAMPLES_DIR):
        tk.Label(dynamic_frame, text="No pre-existing samples found!").pack()
    else:
        sound_files = [f for f in os.listdir(PRE_EXISTING_SAMPLES_DIR) if f.endswith(".wav")]
        for sound in sound_files:
            sound_path = os.path.join(PRE_EXISTING_SAMPLES_DIR, sound)
            tk.Button(dynamic_frame, text=sound, command=lambda sp=sound_path: play_sample(sp)).pack()

    tk.Button(dynamic_frame, text="Next (Generation): Write New Hits!", command=show_duration_slider).pack()

# Function to handle the start button click for generation
def on_start():
    duration = duration_var.get()
    messagebox.showinfo("Processing", f"Generating sound samples of {duration} seconds...")
    output_dir = generate_samples(duration)
    show_generated_samples(output_dir)

# Function to display the menu of generated samples
def show_generated_samples(directory):
    def play_sample(filepath):
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    # Clear the dynamic content area
    clear_dynamic_content()

    tk.Label(dynamic_frame, text="Generated Sound Samples").pack()

    # List sound files in the directory
    sound_files = [f for f in os.listdir(directory) if f.endswith(".wav")]
    for sound in sound_files:
        sound_path = os.path.join(directory, sound)
        tk.Button(dynamic_frame, text=sound, command=lambda sp=sound_path: play_sample(sp)).pack()

    tk.Button(dynamic_frame, text="Exit", command=root.destroy).pack()

# Function to display the duration slider and start generation
def show_duration_slider():
    # Clear the dynamic content area
    clear_dynamic_content()

    tk.Label(dynamic_frame, text="Select Duration (5-60 seconds):").pack()
    duration_slider = tk.Scale(dynamic_frame, from_=5, to=60, orient="horizontal", variable=duration_var)
    duration_slider.pack()

    tk.Button(dynamic_frame, text="Start Generating Samples", command=on_start).pack()

# Utility function to clear dynamic content
def clear_dynamic_content():
    for widget in dynamic_frame.winfo_children():
        widget.destroy()

# Main window
root = tk.Tk()

root.title("The Next Generation Jazz Band")

root.geometry("800x600")
# Load and display the main image
image_path = projectpath / "assets" / "jazz_club.png"  # Replace with your image file path
try:
    main_image = Image.open(image_path)
    main_image = main_image.resize((400, 200))  # Resize image to fit the window
    main_image_tk = ImageTk.PhotoImage(main_image)
    image_label = tk.Label(root, image=main_image_tk)
    image_label.pack()
except FileNotFoundError:
    tk.Label(root, text="Image not found!").pack()

# Dynamic content frame
dynamic_frame = tk.Frame(root)
dynamic_frame.pack()

# Variable for duration slider
duration_var = tk.IntVar(value=5)

# Start with existing samples menu
show_existing_samples()

# Run the UI
root.mainloop()