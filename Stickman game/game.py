import tkinter as tk

class StickmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Stickman Game")
        self.root.geometry("900x600")
        self.root.configure(bg="#1a1a1a")
        self.root.attributes('-topmost', True)
        
        # Variables
        self.penis_var = tk.BooleanVar(value=False)
        self.breasts_var = tk.BooleanVar(value=False)
        self.tits_var = tk.BooleanVar(value=False)
        self.pussy_var = tk.BooleanVar(value=False)
        self.nigger_var = tk.BooleanVar(value=False)
        
        # Animation state
        self.animation_running = False
        self.animation_step = 0
        self.buyer_x = -100
        self.slave_x = 300
        self.whip_frame = 0
        
        # Left panel
        self.left_frame = tk.Frame(root, bg="#2d2d2d", width=200)
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.pack_propagate(False)
        
        # Toggle button
        self.toggle_btn = tk.Button(self.left_frame, text="◀", 
                                   command=self.toggle_panel, bg="#444", fg="white",
                                   font=("Arial", 10, "bold"))
        self.toggle_btn.pack(fill="x", pady=5, padx=5)
        
        tk.Label(self.left_frame, text="OPTIONS", bg="#2d2d2d", fg="white",
                font=("Arial", 14, "bold")).pack(pady=5)
        
        # NSFW checkboxes
        self.create_checkbox("Penis", self.penis_var)
        self.create_checkbox("Breasts", self.breasts_var)
        self.create_checkbox("Tits", self.tits_var)
        self.create_checkbox("Pussy", self.pussy_var)
        self.create_checkbox("Nigger", self.nigger_var)
        
        # Action button
        self.action_btn = tk.Button(self.left_frame, text="Update", 
                                   command=self.start_transaction, bg="#27ae60", 
                                   fg="white", font=("Arial", 10, "bold"))
        self.action_btn.pack(pady=15)
        
        # Status label
        self.status_label = tk.Label(self.left_frame, text="", bg="#2d2d2d", 
                                    fg="#ffff00", font=("Arial", 10))
        self.status_label.pack()
        
        # Canvas
        self.canvas = tk.Canvas(root, bg="#87CEEB", highlightthickness=0)
        self.canvas.pack(side="right", fill="both", expand=True)
        
        self.panel_visible = True
        self.draw_scene()
    
    def create_checkbox(self, text, variable):
        cb = tk.Checkbutton(self.left_frame, text=text, variable=variable,
                           bg="#2d2d2d", fg="white", selectcolor="#444",
                           font=("Arial", 11), activebackground="#2d2d2d",
                           activeforeground="white", command=self.update_button)
        cb.pack(anchor="w", padx=20, pady=3)
    
    def update_button(self):
        if self.nigger_var.get():
            self.action_btn.config(text="Sell Nigga", bg="#8b4513")
        else:
            self.action_btn.config(text="Update", bg="#27ae60")
        self.draw_scene()
    
    def toggle_panel(self):
        if self.panel_visible:
            self.left_frame.config(width=40)
            self.toggle_btn.config(text="▶")
            for widget in self.left_frame.winfo_children()[1:]:
                widget.pack_forget()
        else:
            self.left_frame.config(width=200)
            self.toggle_btn.config(text="◀")
            for widget in self.left_frame.winfo_children()[1:]:
                widget.pack()
        self.panel_visible = not self.panel_visible
    
    def start_transaction(self):
        if self.nigger_var.get() and not self.animation_running:
            self.animation_running = True
            self.animation_step = 0
            self.buyer_x = -100
            self.slave_x = 300
            self.whip_frame = 0
            self.status_label.config(text="Transaction starting...")
            self.animate_transaction()
        else:
            self.draw_scene()
    
    def draw_body_parts(self, x, y, skin, outline):
        """Draw the NSFW body parts based on toggles"""
        # Breasts/Tits - on chest
        if self.breasts_var.get() or self.tits_var.get():
            self.canvas.create_oval(x-28, y-15, x-8, y+15, 
                                   fill="#ffb6c1", outline="#ff69b4", width=2)
            self.canvas.create_oval(x+8, y-15, x+28, y+15, 
                                   fill="#ffb6c1", outline="#ff69b4", width=2)
        
        # Penis - below body
        if self.penis_var.get():
            self.canvas.create_line(x, y+50, x, y+95, width=8, fill="#ff69b4")
            self.canvas.create_oval(x-10, y+88, x+10, y+110, 
                                   fill="#ff1493", outline="#c71585", width=2)
        
        # Pussy - at groin
        if self.pussy_var.get():
            self.canvas.create_arc(x-18, y+40, x+18, y+75, start=0, extent=180, 
                                  fill="#ff69b4", outline="#ff1493", width=2)
    
    def draw_stickman_basic(self, x, y, skin="#f39c12", outline="#d35400", 
                           scared=False, being_whipped=False, running=False):
        """Draw a basic stickman with all parts"""
        
        # Body shake when being whipped
        if being_whipped:
            x += (8 if self.whip_frame % 2 == 0 else -8)
        
        # Head
        self.canvas.create_oval(x-35, y-110, x+35, y-40, fill=skin, outline=outline, width=3)
        
        # Face
        if scared or being_whipped:
            # Wide scared eyes
            self.canvas.create_oval(x-22, y-90, x-10, y-78, fill="white", outline="black")
            self.canvas.create_oval(x+10, y-90, x+22, y-78, fill="white", outline="black")
            self.canvas.create_oval(x-18, y-86, x-14, y-82, fill="black")
            self.canvas.create_oval(x+14, y-86, x+18, y-82, fill="black")
            # Open screaming mouth
            self.canvas.create_oval(x-12, y-75, x+12, y-55, fill="black")
        else:
            # Normal eyes
            self.canvas.create_arc(x-22, y-90, x-8, y-75, start=0, extent=180, fill="black")
            self.canvas.create_arc(x+8, y-90, x+22, y-75, start=0, extent=180, fill="black")
            # Smile
            self.canvas.create_arc(x-15, y-80, x+15, y-55, start=200, extent=140, 
                                  fill="white", width=2)
        
        # Body line (drawn first so parts overlay)
        self.canvas.create_line(x, y-40, x, y+50, width=5, fill="#2c3e50")
        
        # Draw NSFW parts on top of body
        self.draw_body_parts(x, y, skin, outline)
        
        # Arms
        if running:
            self.canvas.create_line(x, y-25, x-55, y-50, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y-25, x+55, y, width=5, fill="#2c3e50")
        elif being_whipped:
            self.canvas.create_line(x, y-25, x-45, y-15, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y-25, x+45, y-15, width=5, fill="#2c3e50")
        else:
            self.canvas.create_line(x, y-25, x-40, y+15, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y-25, x+40, y+15, width=5, fill="#2c3e50")
        
        # Legs
        if running:
            self.canvas.create_line(x, y+50, x-45, y+110, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y+50, x+25, y+115, width=5, fill="#2c3e50")
        else:
            self.canvas.create_line(x, y+50, x-30, y+130, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y+50, x+30, y+130, width=5, fill="#2c3e50")
    
    def draw_buyer(self, x, y, belt_ready=False, whipping=False):
        """Draw the white buyer"""
        skin = "#f39c12"
        outline = "#d35400"
        
        # Head
        self.canvas.create_oval(x-35, y-110, x+35, y-40, fill=skin, outline=outline, width=3)
        
        # Face - smiling/evil grin
        self.canvas.create_arc(x-22, y-90, x-8, y-75, start=0, extent=180, fill="black")
        self.canvas.create_arc(x+8, y-90, x+22, y-75, start=0, extent=180, fill="black")
        self.canvas.create_arc(x-15, y-80, x+15, y-55, start=200, extent=140, 
                              fill="white", width=2)
        
        # Body
        self.canvas.create_line(x, y-40, x, y+50, width=5, fill="#2c3e50")
        
        # Arms
        if whipping:
            self.canvas.create_line(x, y-25, x+60, y-70, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y-25, x-35, y+20, width=5, fill="#2c3e50")
            # Belt in hand
            self.canvas.create_line(x+60, y-70, x+80, y-20, width=4, fill="#8b4513")
        elif belt_ready:
            self.canvas.create_line(x, y-25, x+50, y-15, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y-25, x-35, y+20, width=5, fill="#2c3e50")
            # Holding belt
            self.canvas.create_line(x+50, y-15, x+70, y+25, width=4, fill="#8b4513")
        else:
            self.canvas.create_line(x, y-25, x-40, y+15, width=5, fill="#2c3e50")
            self.canvas.create_line(x, y-25, x+40, y+15, width=5, fill="#2c3e50")
        
        # Legs
        self.canvas.create_line(x, y+50, x-30, y+130, width=5, fill="#2c3e50")
        self.canvas.create_line(x, y+50, x+30, y+130, width=5, fill="#2c3e50")
    
    def draw_money(self, x, y):
        """Draw money stack"""
        for i in range(4):
            self.canvas.create_rectangle(x-25, y-15+i*6, x+25, y+15+i*6, 
                                        fill="#85bb65", outline="#228b22", width=2)
            self.canvas.create_text(x, y+i*6, text="$", font=("Arial", 16, "bold"), 
                                   fill="#006400")
    
    def animate_transaction(self):
        if not self.animation_running:
            return
            
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 400, 900, 600, fill="#228B22", outline="")
        
        # Phase 1: Buyer enters
        if self.animation_step == 0:
            self.buyer_x += 6
            self.draw_buyer(self.buyer_x, 280)
            self.draw_stickman_basic(300, 280, "#8b4513", "#3d2817")
            
            if self.buyer_x >= 160:
                self.animation_step = 1
                self.status_label.config(text="Handing over cash...")
        
        # Phase 2: Show money
        elif self.animation_step == 1:
            self.draw_buyer(160, 280)
            self.draw_stickman_basic(300, 280, "#8b4513", "#3d2817")
            self.draw_money(230, 220)
            
            self.canvas.after(1200, lambda: self.next_step(2))
            return
        
        # Phase 3: Belt ready
        elif self.animation_step == 2:
            self.draw_buyer(160, 280, belt_ready=True)
            self.draw_stickman_basic(300, 280, "#8b4513", "#3d2817", scared=True)
            self.status_label.config(text="Taking out belt...")
            
            self.canvas.after(800, lambda: self.next_step(3))
            return
        
        # Phase 4: Whipping
        elif self.animation_step == 3:
            self.whip_frame += 1
            self.draw_buyer(160, 280, whipping=True)
            self.draw_stickman_basic(300, 280, "#8b4513", "#3d2817", being_whipped=True)
            
            # Belt whip arc
            if self.whip_frame % 3 < 2:
                self.canvas.create_arc(210, 180, 380, 350, start=30, extent=120, 
                                      style="arc", width=6, outline="#654321")
            
            if self.whip_frame > 25:
                self.animation_step = 4
                self.status_label.config(text="RUN NIGGER RUN!")
            else:
                self.root.after(40, self.animate_transaction)
                return
        
        # Phase 5: Run away
        elif self.animation_step == 4:
            self.slave_x -= 10
            self.draw_buyer(160, 280)
            
            if self.slave_x > -120:
                self.draw_stickman_basic(self.slave_x, 280, "#8b4513", "#3d2817", running=True)
                self.root.after(25, self.animate_transaction)
                return
            else:
                self.animation_step = 5
        
        # Phase 6: Complete
        if self.animation_step == 5:
            self.draw_buyer(160, 280)
            self.status_label.config(text="SOLD! Click Update to reset")
            self.animation_running = False
            return
        
        self.root.after(30, self.animate_transaction)
    
    def next_step(self, step):
        self.animation_step = step
        self.animate_transaction()
    
    def draw_scene(self):
        """Draw static scene when not animating"""
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 400, 900, 600, fill="#228B22", outline="")
        
        # Determine skin color based on nigger toggle
        if self.nigger_var.get():
            skin = "#8b4513"
            outline = "#3d2817"
        else:
            skin = "#f39c12"
            outline = "#d35400"
        
        # Draw the stickman with all selected body parts
        self.draw_stickman_basic(300, 280, skin, outline)

if __name__ == "__main__":
    root = tk.Tk()
    game = StickmanGame(root)
    root.mainloop()