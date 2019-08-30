from collections import Counter


offers = {'A': {1:50, 3:130, 5:200}, 'B': {1:30, 2:45}, 'C': {1:20}, 'D':{1:15},
          'E': {1:40, 2:'B'}, 'F': {1:10, 2:'F'}, 'G': {1:20}, 'H': {1:10, 5:45, 10:80},
          'I': {1:35}, 'J': {1:60}, 'K': {1:70, 2:120}, 'L': {1:90}, 'M': {1:15},
          'N': {1:40, 3:'M'}, 'O': {1:10}, 'P': {1:50, 5:200}, 'Q': {1:30, 3:80},
          'R': {1:50, 3:'Q'}, 'S': {1:20}, 'T': {1:20}, 'U': {1:40, 3:'U'},
          'V': {1:50, 2:90, 3:130}, 'W': {1:20}, 'X': {1:17}, 'Y': {1:20}, 'Z': {1:21}}


def difference(a, b):
    countA = Counter(a)
    countB = Counter(b)
    countC = {}

    for prod, n in countA.items():
        try:
            m = countB[prod]
            countC[prod] = n-m
        except KeyError:
            countC[prod] = n

    return countC


def checkout(sku):

    products = list(offers.keys())
    price = 0

    # catching invalid input
    if not set(list(sku)) <= set(products):
        return -1

    # 1. Managing group offers
    # items from most expansive to cheapest
    group = ['Z', 'T', 'S', 'Y', 'X']
    groupOffer = [x for x in list(sku) if x in group]

    # sorting group offer according to the order in group
    groupOffer = sorted(groupOffer, key=lambda x: group.index(x))

    # count the number of each item
    countG = Counter(groupOffer)

    # resorting groupOffer according to repetition and removing duplicates
    groupOffer = sorted(groupOffer, key=lambda x: -countG[x])

    while True:
        deleted = []

        for item in groupOffer:

            # make sure we only take 3 items from there
            if len(deleted) == 3:
                break

            if item in sku:
                indx = sku.index(item)
                # adding the item to the delete list
                deleted.append(indx)

        deleted = sorted(deleted, key=lambda x: -x)

        if len(deleted) == 3:
            for indx in deleted:
                sku = sku[:indx] + sku[indx+1:]
            price += 45

        else:
            break

    # 2. Managing the free items first
    # the items that are for free
    count = Counter(sku)
    free = ''

    for product, n in count.items():

        keys = list(offers[product].keys())

        # sorting the offers from higher to lower
        keys = sorted(keys, key=lambda x: -x)

        for key in keys:

            while n // key > 0:
                # number of times that offer <key> fits in <n>

                offer = offers[product][key]

                # if the free product is the same product, check that there are
                # at least one more in the list before removing it
                if product == offer:
                    # if the offer is a free product
                    if type(offer) == str and n > key:
                        free += offer

                # if the products are difference, add it to the free list directly
                else:
                    # if the offer is a free product
                    if type(offer) == str:
                        free += offer

                # updating the number of items left
                n -= key

            if n == 0:
                break

    # the items to pay
    unfree = difference(sku, free)

    # get the product and its number of appearances
    for product, n in unfree.items():

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