"""
This is an ugly short-term solution for testing purposes
Rather than building a user interface & input that's not going to be any use when the testing is over,
this is a couple of variables containing the raw text of the testing data
"""

## raw text of wishlist
pageOne = """iority	Game ID	Title	Start Time	Duration	Cost
	RPG24ND260320	Psychic Trash Detectives	Friday	3 hr	$8
		Psychic Trash Detectives, 1st Edition	10:00 AM EDT		
	RPG24ND257534	The Monster is What We Make of It	Thursday	4 hr	$4
		Tales From the Loop, 1st Edition	7:00 PM EDT		
	RPG24ND245067	WHPA–TV13: Nightmares at the Public-Access Station	Thursday	2 hr	$2
		Weird Heroes of Public Access, 1st Edition	8:00 PM EDT		
	RPG24ND250874	A Winter Carcass	Friday	4 hr	$4
		TimeWatch, 1st Edition	9:00 AM EDT		
	RPG24ND244741	Dad Overboard	Friday	4 hr	$4
		Brindlewood Bay, 1st Edition	6:00 PM EDT		
	RPG24ND263533	Dad Overboard	Saturday	4 hr	$6
		Brindlewood Bay, 1st Edition	3:00 PM EDT		
	RPG24ND263532	Dad Overboard	Thursday	4 hr	$6
		Brindlewood Bay, 1st Edition	3:00 PM EDT		
	RPG24ND255351	How to Create a World with Friends	Thursday	2 hr	$2
		The Quiet Year, 1st Edition	2:00 PM EDT		
	RPG24ND254659	The Dunwich Hotel	Thursday	3 hr	$4
		It Came From The Late Late Late Show, 1st Edition	2:00 PM EDT		
	RPG24ND258234	Tomorrow's Messenger	Sunday	4 hr	$8
		Cypher System, 1st Edition	12:00 PM EDT		
	RPG24ND265879	Fun and Games	Thursday	4 hr	$10
		Rapscallion, 1st Edition	6:00 PM EDT		
	RPG24ND265938	Fun and Games	Friday	4 hr	$10
		Rapscallion, 1st Edition	2:00 PM EDT		
	RPG24ND265968	Fun and Games	Friday	4 hr	$10
		Rapscallion, 1st Edition	6:00 PM EDT		
	RPG24ND265999	Fun and Games	Saturday	4 hr	$10
		Rapscallion, 1st Edition	10:00 AM EDT		
	RPG24ND265969	Victoria's Sinking	Friday	4 hr	$10
		Rapscallion, 1st Edition	6:00 PM EDT		
	RPG24ND265849	Victoria's Sinking	Thursday	4 hr	$10
		Rapscallion, 1st Edition	2:00 PM EDT		
	RPG24ND265998	Victoria's Sinking	Saturday	4 hr	$10
		Rapscallion, 1st Edition	10:00 AM EDT		
	RPG24ND266059	Victoria's Sinking	Saturday	4 hr	$10
		Rapscallion, 1st Edition	6:00 PM EDT		
	RPG24ND253095	Crazy Dog Guards the Gate	Sunday	4 hr	$10
		Coyote and Crow, 1st Edition	10:00 AM EDT		
	RPG24ND266085	Hide and Seek	Sunday	4 hr	$10
		Masks: A New Generation, 1st Edition	10:00 AM EDT		
	RPG24ND265905	Into Dimension X!	Friday	4 hr	$10
		Masks: A New Generation, 1st Edition	10:00 AM EDT		
	RPG24ND265875	Hide and Seek	Thursday	4 hr	$10
		Masks: A New Generation, 1st Edition	6:00 PM EDT		
	RPG24ND266025	Into Dimension X!	Saturday	4 hr	$10
		Masks: A New Generation, 1st Edition	2:00 PM EDT		
	RPG24ND253080	In Grandfather's Shadow	Saturday	3 hr	$10
		Coyote and Crow, 1st Edition	10:00 AM EDT		
	RPG24ND253064	What's the Damage?	Thursday	3 hr	$
		Coyote and Crow, 1st Edition	10:00 AM EDT		
"""

pageTwo = """ority	Game ID	Title	Start Time	Duration	Cost
	RPG24ND258115	Tomorrow's Messenger	Thursday	4 hr	$8
		Cypher System, 1st Edition	10:00 AM EDT		
	RPG24ND266069	A Cook's Tale	Saturday	4 hr	$10
		Root: the RPG, 1st Edition	6:00 PM EDT		
	RPG24ND266058	Beneath Cruel Tides	Saturday	4 hr	$10
		Rapscallion, 1st Edition	6:00 PM EDT		
	RPG24ND258235	Best Leave Them Ghosts Alone	Thursday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	12:00 PM EDT		
	RPG24ND258084	Best Leave Them Ghosts Alone	Thursday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	2:00 PM EDT		
	RPG24ND258096	Best Leave Them Ghosts Alone	Thursday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	6:00 PM EDT		
	RPG24ND258236	Best Leave Them Ghosts Alone	Thursday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	4:00 PM EDT		
	RPG24ND258240	Best Leave Them Ghosts Alone	Friday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	12:00 PM EDT		
	RPG24ND258183	Best Leave Them Ghosts Alone	Friday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	10:00 AM EDT		
	RPG24ND258242	Best Leave Them Ghosts Alone	Friday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	4:00 PM EDT		
	RPG24ND258184	Best Leave Them Ghosts Alone	Friday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	2:00 PM EDT		
	RPG24ND258243	Best Leave Them Ghosts Alone	Friday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	8:00 PM EDT		
	RPG24ND258185	Best Leave Them Ghosts Alone	Friday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	6:00 PM EDT		
	RPG24ND258245	Best Leave Them Ghosts Alone	Saturday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	12:00 PM EDT		
	RPG24ND258186	Best Leave Them Ghosts Alone	Saturday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	10:00 AM EDT		
	RPG24ND258246	Best Leave Them Ghosts Alone	Saturday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	4:00 PM EDT		
	RPG24ND258187	Best Leave Them Ghosts Alone	Saturday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	2:00 PM EDT		
	RPG24ND258247	Best Leave Them Ghosts Alone	Saturday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	8:00 PM EDT		
	RPG24ND258188	Best Leave Them Ghosts Alone	Saturday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	6:00 PM EDT		
	RPG24ND258189	Best Leave Them Ghosts Alone	Sunday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	10:00 AM EDT		
	RPG24ND258248	Best Leave Them Ghosts Alone	Sunday	4 hr	$8
		Old Gods of Appalachia, 1st Edition	12:00 PM EDT		
	ZED24ND250490	Dragonlance: New Book 3 Weis & Hickman Novel Unboxing	Thursday	15 min	$32
			8:00 AM EDT		
	ENT24ND250491	Weis & Hickman Classic Dragonlance Celebration	Saturday	1 hr	$4
			2:00 PM EDT		
	SEM24ND266767	Running your first PbtA Game	Thursday	1 hr	$0
			11:00 AM EDT		
	SEM24ND266770	Designing Playbooks in PbtA	Thursday	1 hr 30 min	$
			2:00 PM EDT		
"""