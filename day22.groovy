from graphviz import Digraph
dot = Digraph()

dot.node('A', '🎅 Start: Historians Need Device!')
dot.node('B', '🐒 Encounter Mischievous Monkey')
dot.node('T', '🗣️ Monkey Translator App')
dot.node('C', '🍌 Monkey Demands Bananas')
dot.node('D', '🧮 Calculate Required Bananas')
dot.node('E', '⚡ Apply Bitwise Operations')
dot.node('N1', '📝 Log Banana Demands in Notion')
dot.node('N2', '📊 Track Calculations in Tables')
dot.node('F', '🤔 Do We Have Enough Bananas?')
dot.node('G', '🤝 Exchange Bananas')
dot.node('H', '🍌 Collect More Bananas')
dot.node('I', '📱 Get Device Back')
dot.node('J', '🎊 Save Christmas!')
dot.node('K', '🙈 Translate Monkey Dance')
dot.node('L', '🔄 Shift Bits Left')
dot.node('M', '🔄 Shift Bits Right')
dot.node('N3', '👥 Team Collaboration')
dot.node('N4', '⏰ Set Banana Collection Reminders')
dot.node('N5', '📱 Mobile Sync')
dot.node('N6', '📄 Document Success in Notion')
dot.node('N7', '📝 Save Monkey Phrases')

dot.edges([
	'AB', 'BT', 'TC', 'CD', 'DE', 'DF', 'FG', 'FH', 'HI', 'IJ', 'TK', 'KD', 
	'EL', 'LM', 'ME', 'DN1', 'EN2', 'N3N1', 'N3N2', 'N4H', 'N5N1', 'JN6', 
	'TN7', 'N7N1'
])

dot.render('flowchart', format='png', view=True)