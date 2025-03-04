import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict

class RotationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Equal Time Football Planner")
        
        # Input Fields
        ttk.Label(root, text="Game Structure:").grid(row=0, column=0, padx=10, pady=5)
        self.segment_var = ttk.Combobox(root, values=["Quarters (4)", "Halves (2)"])
        self.segment_var.grid(row=0, column=1, padx=10, pady=5)
        self.segment_var.bind("<<ComboboxSelected>>", self.update_gk_options)
        
        ttk.Label(root, text="Players Per Side:").grid(row=1, column=0, padx=10, pady=5)
        self.players_side_var = ttk.Combobox(root, values=["5-a-side", "6-a-side", "7-a-side"])
        self.players_side_var.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Number of Goalkeepers:").grid(row=2, column=0, padx=10, pady=5)
        self.gk_count_var = ttk.Combobox(root, values=[])
        self.gk_count_var.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Player Names (comma-separated):").grid(row=3, column=0, padx=10, pady=5)
        self.players_entry = ttk.Entry(root, width=40)
        self.players_entry.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Captain:").grid(row=4, column=0, padx=10, pady=5)
        self.captain_var = ttk.Combobox(root)
        self.captain_var.grid(row=4, column=1, padx=10, pady=5)
        
        # Buttons
        ttk.Button(root, text="Generate Plan", command=self.generate_plan).grid(row=5, column=0, columnspan=2)
        ttk.Button(root, text="Save Plan", command=self.save_plan).grid(row=6, column=0, columnspan=2)
        ttk.Button(root, text="Reset", command=self.clear).grid(row=7, column=0, columnspan=2)
        
        # Results
        self.results_text = tk.Text(root, height=15, width=60)
        self.results_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    
    def update_gk_options(self, event=None):
        """Update goalkeeper count options based on game structure"""
        segments = int(self.segment_var.get().split(" ")[1][1])
        self.gk_count_var['values'] = list(range(1, segments + 1))
    
    def clear(self):
        """Reset all fields"""
        self.segment_var.set('')  # Clear game structure
        self.players_side_var.set('')  # Clear players per side
        self.gk_count_var.set('')  # Clear goalkeeper count
        self.players_entry.delete(0, tk.END)  # Clear player names
        self.captain_var.set('')  # Clear captain selection
        self.captain_var['values'] = []  # Reset captain dropdown options
        self.results_text.delete(1.0, tk.END)  # Clear results
    
    def validate_players(self, players: List[str]) -> bool:
        """Check for unique, non-empty player names"""
        # Strip whitespace and remove empty strings
        players = [name.strip() for name in players if name.strip()]
        
        # Check for duplicates
        if len(players) != len(set(players)):
            messagebox.showerror("Error", "Player names must be unique!")
            return False
        
        # Check for minimum players
        if len(players) < 5:
            messagebox.showerror("Error", "Need at least 5 players!")
            return False
        
        return True
    
    def generate_plan(self):
        """Main logic"""
        try:
            # Get inputs
            players = [p.strip() for p in self.players_entry.get().split(",")]
            if not self.validate_players(players):
                return
            
            # Update captain dropdown
            self.captain_var['values'] = players
            
            # Calculate rotation
            plan = self.calculate_rotation(players)
            
            # Display results
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "⚽ Rotation Plan:\n\n")
            for idx, segment in enumerate(plan["schedule"], 1):
                self.results_text.insert(tk.END, 
                    f"Segment {idx}: GK={segment['goalkeeper']}\n"
                    f"Outfield: {', '.join(segment['outfield_players'])}\n\n")
            
            self.results_text.insert(tk.END, "\n⏱️ Time Breakdown:\n")
            for player, times in plan["times"].items():
                self.results_text.insert(tk.END,
                    f"{player}: GK={times['goalkeeping']}min | Outfield={times['outfield']}min\n")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def save_plan(self):
        """Save the rotation plan to a file"""
        try:
            plan = self.results_text.get(1.0, tk.END)
            with open("rotation_plan.txt", "w") as file:
                file.write(plan)
            messagebox.showinfo("Success", "Plan saved to rotation_plan.txt")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def calculate_rotation(self, players: List[str]) -> Dict:
        """Rotation logic with fair outfield time distribution"""
        segments = int(self.segment_var.get().split(" ")[1][1])
        gk_count = int(self.gk_count_var.get())
        outfield_slots = int(self.players_side_var.get().split("-")[0]) - 1

        # Assign goalkeepers
        goalkeepers = players[:gk_count]
        gk_assignments = [goalkeepers[i % gk_count] for i in range(segments)]

        # Assign outfield players (excluding current goalkeeper)
        outfield_players = [p for p in players if p not in goalkeepers]
        outfield_assignments = []
        for i in range(segments):
            # Current goalkeeper is not available for outfield
            available_players = [p for p in players if p != gk_assignments[i]]
            start = (i * outfield_slots) % len(available_players)
            end = start + outfield_slots
            if end > len(available_players):
                # Wrap around if necessary
                outfield_assignments.append(available_players[start:] + available_players[:end - len(available_players)])
            else:
                outfield_assignments.append(available_players[start:end])

        # Build schedule
        schedule = []
        for i in range(segments):
            schedule.append({
                "goalkeeper": gk_assignments[i],
                "outfield_players": outfield_assignments[i]
            })

        # Calculate time breakdown
        times = {}
        for player in players:
            times[player] = {"goalkeeping": 0, "outfield": 0}

        for segment in schedule:
            times[segment["goalkeeper"]]["goalkeeping"] += 10
            for player in segment["outfield_players"]:
                times[player]["outfield"] += 10

        # Identify players with the least outfield time
        min_outfield_players = sorted(players, key=lambda x: times[x]["outfield"])[:2]  # Top 2 players with least time

        # Redistribute goalkeepers' outfield time to these players
        for player in min_outfield_players:
            for segment in schedule:
                if player not in segment["outfield_players"] and segment["goalkeeper"] in goalkeepers:
                    # Replace a goalkeeper's outfield time with this player
                    segment["outfield_players"][0] = player  # Replace the first outfield player
                    times[segment["goalkeeper"]]["outfield"] -= 10
                    times[player]["outfield"] += 10
                    break

        # Balance time using captain
        target_outfield_time = (segments * 10 * outfield_slots) // (len(players) - gk_count)
        for player in players:
            if player == self.captain_var.get():
                continue
            diff = times[player]["outfield"] - target_outfield_time
            if diff > 0:
                times[player]["outfield"] -= diff
                times[self.captain_var.get()]["outfield"] += diff

        return {"schedule": schedule, "times": times}

if __name__ == "__main__":
    root = tk.Tk()
    app = RotationApp(root)
    root.mainloop()