# # Dictionaries
# # All fun and games keep our crazy x list ... but we also need more info.
# # Introducing dictionaries
#
# # Dictionaries are defined using {}
# # They are organised with keys that point to values
# # Much like looking up something on a dictionary or information about a contact on our phones.
#     # Thus in our phone, the contact Filipe Paiva will hold a lot's of info for this entry.
#     # could be the phone number, work number e-mail, address and so on..
#
# # Syntax
# # variable number = { }
# # dict_name = {'example_key': 'value', }
# # Difining a simple dictionary with two keys
# d_crazy_e = {
#     'Carolina': 'she was actually nice',
#     'Arthur':  'bit of drinker'
#
# }
# print(d_crazy_e)
#
# # Accessing values - use the key!
#
# print(d_crazy_e['Carolina'])
#
# # Adding a new key, pair value
# d_crazy_e['Kile'] = 'Likes monster'
# print(d_crazy_e)
#
# # Get out all of the keys
# print(d_crazy_e.keys())
# # Get out all of the values
# print(d_crazy_e.pop('Kile'))

# Better example of Dictrionary

crazy1 = {
    'name': 'Carolina',
    'phone': '07880490510',
    'address': 'Location 1, at places',
    'Places to avoid': ['Milan', 'Lisbon', 'Taveria']
}
