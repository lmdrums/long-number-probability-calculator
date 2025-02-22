from customtkinter import (CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton, CTkOptionMenu,
                           CTkCheckBox, StringVar, CTkImage, CTkSlider, CTkToplevel, CTkScrollbar,
                           set_appearance_mode, set_default_color_theme, CTkBaseClass, END, CTkTextbox)
import pyperclip

import long_number_probability_calculator.constants as c
import long_number_probability_calculator.helpers as h

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title(c.TITLE)
        self.geometry(c.GEOMETRY)
        
        self.frame = CTkFrame(self)
        self.frame.pack(anchor="center", expand=True, fill="both", padx=10, pady=10)

        self.description = CTkLabel(self.frame,
                                    text=c.DESCRIPTION, font=("Segoe UI", 13),
                                    wraplength=640)
        self.description.grid(column=0, row=0, padx=10, columnspan=3, sticky="w")

        self.n_label = CTkLabel(self.frame, text="Length of random number:", font=c.MAIN_FONT)
        self.n_label.grid(column=0, row=1, sticky="w", pady=(10,0), padx=(10,0))
        self.n_entry = CTkEntry(self.frame, font=c.MAIN_FONT, placeholder_text="Length")
        self.n_entry.grid(column=1, row=1, sticky="w", pady=(10,0), padx=(10,0))
        self.n_slider = CTkSlider(self.frame, from_=0, to=c.MAXIMUM_NUMBER_N,
                                  number_of_steps=c.MAXIMUM_NUMBER_N,
                                  command=self.n_slider_function)
        self.n_slider.grid(column=2, row=1, pady=(10,0), padx=(10,0), sticky="w")
        self.n_slider.set(c.STARTING_VALUE_N)
        self.n_entry.insert(END, c.STARTING_VALUE_N)

        self.m_label = CTkLabel(self.frame, text="Length of target number:", font=c.MAIN_FONT)
        self.m_label.grid(column=0, row=2, sticky="w", pady=(10,0), padx=(10,0))
        self.m_entry = CTkEntry(self.frame, font=c.MAIN_FONT, placeholder_text="Length")
        self.m_entry.grid(column=1, row=2, sticky="w", pady=(10,0), padx=(10,0))
        self.m_slider = CTkSlider(self.frame, from_=1, to=c.MAXIMUM_NUMBER_M,
                                  number_of_steps=c.MAXIMUM_NUMBER_M,
                                  command=self.m_slider_function)
        self.m_slider.grid(column=2, row=2, pady=(10,0), padx=(10,0), sticky="w")
        self.m_slider.set(c.STARTING_VALUE_M)
        self.m_entry.insert(END, c.STARTING_VALUE_M)

        self.d_label = CTkLabel(self.frame, text="Number of possible values for m (1-10):",
                                                font=c.MAIN_FONT)
        self.d_label.grid(column=0, row=3, sticky="w", pady=(10,0), padx=(10,0))
        self.d_entry = CTkEntry(self.frame, font=c.MAIN_FONT, placeholder_text="Length")
        self.d_entry.grid(column=1, row=3, sticky="w", pady=(10,0), padx=(10,0))
        self.d_slider = CTkSlider(self.frame, from_=1, to=c.MAXIMUM_NUMBER_D,
                                  number_of_steps=c.MAXIMUM_NUMBER_D,
                                  command=self.d_slider_function)
        self.d_slider.grid(column=2, row=3, pady=(10,0), padx=(10,0), sticky="w")
        self.d_slider.set(c.STARTING_VALUE_D)
        self.d_entry.insert(END, c.STARTING_VALUE_D)

        self.p_output_label = CTkLabel(self.frame, text="Probability:", font=c.MAIN_FONT)
        self.p_output_label.grid(column=0, row=4, sticky="w", pady=(10,0), padx=(10,0))

        self.p_output = CTkTextbox(self.frame, font=c.MAIN_FONT, height=40, wrap="none", state="disabled")
        self.p_output.grid(column=1, row=4, sticky="ew", pady=(10, 0), padx=(10, 0), columnspan=3)
        self.copy_output = CTkButton(self.frame, text="Copy", font=c.MAIN_FONT, command=self.copy)
        self.copy_output.grid(column=0, row=5, sticky="w", pady=(10,0), padx=(10,0))

        self.n_entry.bind("<KeyRelease>", lambda _: self.n_slider_function(int(self.n_entry.get())))
        self.m_entry.bind("<KeyRelease>", lambda _: self.m_slider_function(int(self.m_entry.get())))
        self.d_entry.bind("<KeyRelease>", lambda _: self.d_slider_function(int(self.d_entry.get())))
        self.calculate_probabilty()

    def n_slider_function(self, value):
        self.n_entry.delete(0,END)
        self.n_entry.insert(END, round(value))
        self.calculate_probabilty()

    def m_slider_function(self, value):
        self.m_entry.delete(0,END)
        self.m_entry.insert(END, round(value))
        self.calculate_probabilty()

    def d_slider_function(self, value):
        self.d_entry.delete(0,END)
        self.d_entry.insert(END, round(value))
        self.calculate_probabilty()

    def calculate_probabilty(self):
        n = int(self.n_entry.get())
        m = int(self.m_entry.get())
        d = int(self.d_entry.get())
        probability = h.calculate(n,m,d)
        self.p_output.configure(state="normal")
        self.p_output.delete("1.0", END)
        self.p_output.insert(END, probability)
        self.p_output.configure(state="disabled")

    def copy(self):
        p = self.p_output.get("1.0", END)
        pyperclip.copy(p)