# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


offers = {'A': {1:50, 3:130, 5:200}, 'B': {1:30, 2:45}, 'C': {1:20}, 'D':{1:15},
          'E': {1:40, 2:'B'}, 'F': {1:10, 2:'F'}, 'G': {1:20}, 'H': {1:10, 5:45, 10:80},
          'I': {1:35}, 'J': {1:60}, 'K': {1:80, 2:150}, 'L': {1:90}, 'M': {1:15},
          'N': {1:40, 3:'M'}, 'O': {1:10}, 'P': {1:50, 5:200}, 'Q': {1:30, 3:80},
          'R': {1:50, 3:'Q'}, 'S': {1:30}, 'T': {1:20}, 'U': {1:40, 3:'U'},
          'V': {1:50, 2:90, 3:130}, 'W': {1:20}, 'X': {1:90}, 'Y': {1:10}, 'Z': {1:50}}


def checkout(skus):

    products = list(offers.keys())

    # catching invalid input
    if not set(list(sku)) <= set(products):
        return -1

    price = 0
    count = Counter(sku)

    # get the product and its number of appearances
    for product, n in count.items():

        keys = list(offers[product].keys())

        # sorting the offers from higher to lower
        keys = sorted(keys, key=lambda x: -x)

        for key in keys:

            # number of times that offer <key> fits in <n>
            m = n // key

            offer = offers[product][key]

            # if the offer is a discount
            if type(offer) == int:
                price += m * offer

                # updating the number of items left
                n -= m * key

            if n == 0:
                break

    return price

    raise NotImplementedError()

