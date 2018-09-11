from source.T6_Trees.P61.PrefixTree import PrefixTree

if __name__ == "__main__":
    tree = PrefixTree()

    keys = {
        'ca',
        'cat',
        'can',
        'cap',
        'out',
        'capacity'
    }

    for w in keys:
        tree.add_key(w, w)

    keys2 = {
        'casda',
        'caat',
        'scan',
        'cdfap',
        'dsout',
        'capacdity',
        'capacit'
    }

    for w in keys | keys2:
        dat = tree.find(w)

        if dat is None:
            print("Key   '%10s ' is not contained in tree!" % w)
        else:
            print("Key   '%10s ' is contained in tree : %s" % (w, dat))


