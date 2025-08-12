# Expanded skill tree with subtopics for each section
from graphviz import Digraph

dot = Digraph(comment="Electrical Engineering Learning Skill Tree")
dot.attr(rankdir='LR', size='12')

# DC Circuit Foundations
dot.node("DC", "1. DC Circuit Foundations")
dot.node("DC1", "Ohm’s Law")
dot.node("DC2", "Series & Parallel Circuits")
dot.node("DC3", "Kirchhoff’s Laws")
dot.node("DC4", "Power Formulas")
dot.node("DC5", "Voltage & Current Dividers")

# AC Circuit Fundamentals
dot.node("AC", "2. AC Circuit Fundamentals")
dot.node("AC1", "DC vs AC")
dot.node("AC2", "Peak, RMS, Average")
dot.node("AC3", "Frequency & Phase")
dot.node("AC4", "Capacitors & Inductors in AC")
dot.node("AC5", "Reactance & Impedance")
dot.node("AC6", "AC Power Types")

# Components & Behavior
dot.node("COMP", "3. Components & Their Behavior")
dot.node("COMP1", "Resistors")
dot.node("COMP2", "Capacitors")
dot.node("COMP3", "Inductors")
dot.node("COMP4", "Diodes")
dot.node("COMP5", "Transistors")
dot.node("COMP6", "Relays & Switches")
dot.node("COMP7", "IC Basics")

# Circuit Analysis Techniques
dot.node("ANAL", "4. Circuit Analysis Techniques")
dot.node("ANAL1", "Thevenin & Norton")
dot.node("ANAL2", "Superposition")
dot.node("ANAL3", "Mesh & Nodal Analysis")
dot.node("ANAL4", "Phasor Diagrams")

# Power & Energy
dot.node("PWR", "5. Power & Energy")
dot.node("PWR1", "Power Supplies")
dot.node("PWR2", "Transformers")
dot.node("PWR3", "Batteries & Charging")
dot.node("PWR4", "Efficiency & Losses")
dot.node("PWR5", "Power Factor")

# Digital Electronics
dot.node("DIGI", "6. Digital Electronics")
dot.node("DIGI1", "Logic Gates & Boolean Algebra")
dot.node("DIGI2", "Flip-Flops & Counters")
dot.node("DIGI3", "Microcontrollers")
dot.node("DIGI4", "DAC & ADC")

# Measurement & Tools
dot.node("TOOLS", "7. Measurement & Tools")
dot.node("TOOLS1", "Multimeter Use")
dot.node("TOOLS2", "Oscilloscope")
dot.node("TOOLS3", "Function Generator")
dot.node("TOOLS4", "Soldering & Breadboarding")
dot.node("TOOLS5", "Reading Datasheets")

# Practical Projects
dot.node("PROJ", "8. Practical Projects")
dot.node("PROJ1", "LED Flasher")
dot.node("PROJ2", "Audio Amplifier")
dot.node("PROJ3", "Power Supply Unit")
dot.node("PROJ4", "Radio Receiver")
dot.node("PROJ5", "Arduino Motor Control")

# Advanced Topics
dot.node("ADV", "9. Advanced Topics")
dot.node("ADV1", "Signal Processing")
dot.node("ADV2", "Control Systems")
dot.node("ADV3", "PCB Design")
dot.node("ADV4", "Power Electronics")
dot.node("ADV5", "Embedded Systems & IoT")

# Connections between main sections
dot.edges([("DC", "AC"), ("AC", "COMP"), ("COMP", "ANAL"), ("ANAL", "PWR"), 
           ("PWR", "DIGI"), ("DIGI", "TOOLS"), ("TOOLS", "PROJ"), ("PROJ", "ADV")])

# Subtopic connections for DC
dot.edges([("DC", "DC1"), ("DC", "DC2"), ("DC", "DC3"), ("DC", "DC4"), ("DC", "DC5")])

# Subtopic connections for AC
dot.edges([("AC", "AC1"), ("AC", "AC2"), ("AC", "AC3"), ("AC", "AC4"), ("AC", "AC5"), ("AC", "AC6")])

# Subtopic connections for Components
dot.edges([("COMP", "COMP1"), ("COMP", "COMP2"), ("COMP", "COMP3"), ("COMP", "COMP4"),
           ("COMP", "COMP5"), ("COMP", "COMP6"), ("COMP", "COMP7")])

# Subtopic connections for Analysis
dot.edges([("ANAL", "ANAL1"), ("ANAL", "ANAL2"), ("ANAL", "ANAL3"), ("ANAL", "ANAL4")])

# Subtopic connections for Power
dot.edges([("PWR", "PWR1"), ("PWR", "PWR2"), ("PWR", "PWR3"), ("PWR", "PWR4"), ("PWR", "PWR5")])

# Subtopic connections for Digital
dot.edges([("DIGI", "DIGI1"), ("DIGI", "DIGI2"), ("DIGI", "DIGI3"), ("DIGI", "DIGI4")])

# Subtopic connections for Tools
dot.edges([("TOOLS", "TOOLS1"), ("TOOLS", "TOOLS2"), ("TOOLS", "TOOLS3"), ("TOOLS", "TOOLS4"), ("TOOLS", "TOOLS5")])

# Subtopic connections for Projects
dot.edges([("PROJ", "PROJ1"), ("PROJ", "PROJ2"), ("PROJ", "PROJ3"), ("PROJ", "PROJ4"), ("PROJ", "PROJ5")])

# Subtopic connections for Advanced
dot.edges([("ADV", "ADV1"), ("ADV", "ADV2"), ("ADV", "ADV3"), ("ADV", "ADV4"), ("ADV", "ADV5")])

# Render expanded skill tree
output_path_expanded = "/mnt/data/electrical_engineering_skill_tree"
dot.render(output_path_expanded, format="png", cleanup=True)

output_path_expanded + ".png"
