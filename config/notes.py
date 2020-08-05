-make a commander rec page
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

- optomize commander queries lookup
#     -add name and img_url to commander fields used a lot
    # -add indexes where needed

-finish card detail page
    # -if commander show what cards you own and need

-rework visual cards
    -on hover display link and card_count

-re input allcards data 
#     -add is commander column
#     -add imageurl column
        # -add crads to dtabase

-rework images
    # -format names correctly
    # -add images for specific sets
    # - resize cards in folder

-rework card sets
    # -need full name of sets displayed
    # -need to specify duplicate printings fore correct sets
    -display new card sets and create all sets page

-rework cards owned
    -add column for card in decks, cards not in deck and total cards
    -add total cards

-miscallenous addons
    -login redirect when trying to add cards
    # -automate react build to django
    -make a footer
    -create a banner
    - usercards card_count wont update when switching visual mode

-searchbar
    -improve search(display closest match first)
    -highlight words searched
    -dropdown on rigth click not close
    -display no results if database has no matches

-finsih home page

-finish log in page/log out / register
-fix issue with javascript getelement by id ouf user-image 
    -when not logged in div not displayed search throws error. for now creating a hidden div


VERSION 2
    -use black fro code formating
    -break project up into smaller apps 
    -solitaire card display
    -show only ome hundred popular commanders first then if user wants show rest(speeds up rec)