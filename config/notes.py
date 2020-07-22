# -make a commander rec page
#     -decks html page 
#     -react request for decks close to completing
#         -get all user cards 
#         -get all commander decks
#             -create finalCommanderCount = []
#             -for each commander in commanderDecks
#                 deck = {}
#                 commander = deck['commander_id']
#                 total_cards_owned = 0
#                 cards_owned = []
#                 cards_not_owned = []

# - optomize commander queries lookup
#     -add name and img_url to commander fields used a lot
#     -add card name to usercards database

-finish card detail page
    -has link to commander if is commander
    -if commander show what cards you own and need

-rework visual cards
    -on hover display link and card_count

# -re input allcards data 
#     -add is commander column
#     -add imageurl column
        # -add crads to dtabase

# -re work edh_rec commander info

# -rework images
    # -format names correctly
    # -add images for specific sets
    # - resize cards in folder

-rework card sets
    # -need full name of sets displayed
    # -need to specify duplicate printings fore correct sets
    -display new card sets and create all sets page

-rework cards owned
    -add column for card in decks, cards not in deck and total cards

-miscallenous addons
    -login redirect when trying to add cards
    # -automate react build to django
    -make a footer
    -create a banner
    - usercards card_count wont update when switching visual mode

-cards and search need different endpoints

-searchbar
    -improve search(display closest match first)
    -highlight words searched
    -dropdown on rigth click not close

-finish search page

-finsih home page

-finish log in page/log out / register
-fix issue with javascript getelement by id ouf user-image 
    -when not logged in div not displayed search throws error. for now creating a hidden div


version 2
    -rename apps to be pep8 compliant all lower case no dash
    -break project up into smaller apps 
    -solitaire card display