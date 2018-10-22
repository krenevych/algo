from source.T6_Trees.P2_BinaryTree.L4_SearchTree import SearchTree


class SearchTreeWithDelete(SearchTree):
    """ Розширення класу бінарного дерева можливістю видаляти елементи """


    def removeChild(self, item):
        """ Видаляє сина із заданим значенням навантаження

        :param item: Навантаження
        :return: None
        """
        if self.hasLeft() and self.leftItem() == item:
            self.removeLeft()
        elif self.hasRight() and self.rightItem() == item:
            self.removeRight()

    def delete(self, item):
        """ Видаляє заданий елемент у бінарному дереві

        :param item: Елемент, який потрібно видалити з бінарного дерева
        :return: None
        """
        self.__delete_helper(self, None, item)

    def __search_helper2(self, sub_tree, parent, item):
        """ Допоміжний рекурсивний метод, пошуку заданого елементу у піддереві.

            Відрізняється від метода __search_helper() батьківського класу тим, що передає
            посилання на батьківський елемент вузол, що використовується для видалення елементів з дерева пошуку.

        :param sub_tree: Піддерево у якому здійснюється пошук
        :param parent: Допоміжний параметр, що містить посилання на батьківський вузол
        :param item: Шуканий елемент
        :return: Пару - посилання на знайдений вузол що містить item та батьківський вузол.
        """

        if sub_tree.empty():  # якщо піддерево з коренем sub_tree порожнє, а отже
            return None, None  # елемент item не знайдено повертаємо None
        else:
            node = sub_tree.item()  # беремо навантаження піддерева sub_tree
            if node == item:  # якщо node є шуканим елементом,
                return sub_tree, parent  # повертаємо знайдений вузол та його предка
            elif item < node:  # випадок: шуканий елемент може міститися у лівому піддереві
                if sub_tree.hasLeft():  # якщо дерево має лівого нащадка
                    #  запускаємо рекурсивний пошук item у лівому піддереві
                    return self.__search_helper2(sub_tree.leftChild(), sub_tree, item)
                else:  # якщо дерево не має лівого нащадка
                    return None, None  # дерево не містить шуканого елемента item
            else:  # випадок: шуканий елемент може міститися у правому піддереві
                if sub_tree.hasRight():  # якщо дерево має правого нащадка
                    #  запускаємо рекурсивний пошук item у правому піддереві
                    return self.__search_helper2(sub_tree.rightChild(), sub_tree, item)
                else:  # якщо дерево не має правого нащадка
                    return None, None  # дерево не містить шуканого елемента item

    def __search_max(self, sub_tree, parent):
        """ Допоміжний рекурсивний метод пошуку найбільшого вузла у заданому піддереві.

            Згідно з властивостями бінарного дерева пошука, максимальний елемент може бути
            знайдений при проходженні дерева в глиб рухаючись лише по правих нащадках
        :param sub_tree: Піддерево
        :param parent: Допоміжний параметр, що містить посилання на батьківський вузол
        :return: пару - посилання на знайдений елемент та його предка.
        """

        if sub_tree.hasRight():
            return self.__search_max(sub_tree.rightChild(), sub_tree)
        else:
            # Якщо вузол немає правого нащадка, то він має найбільше навантаження
            return sub_tree, parent

    def __delete_helper(self, sub_tree, parent, item):
        """ Допоміжний рекурсиввий метод, що видаляє заданий елемент з дерева у заданому піддереві
            якщо такий елемент міситься у деремі. Пошук розпочинається з піддерева,
        що має коренем вершину startNode. Для технічних цілей передаємо у підпрограму
        предка вузла startNode - parent

        :param sub_tree: Піддеремо у якому потрібно видалити заданий елемент
        :param parent: Допоміжний параметр, що містить посилання на батьківський вузол
        :param item: Елемент, який потрібно видалити
        :return: None
        """
        # Знаходимо вузол, який треба видалити (також запам'ятовуємо його предка)
        found_item, found_parent = self.__search_helper2(sub_tree, parent, item)

        # Якщо шуканий елемент не міститься у дереві, то припиняємо роботу підпрограми
        if found_item is None:
            return

        if found_item.hasNoChildren():   # Якщо знайдений вузол - листок (немає нащадків)
            if found_parent is None:       # Якщо предок - корінь всього дерева
                found_item.mData = None
            else:
                found_parent.removeChild(found_item.item()) # Видаляєм знайдений елемент

        elif found_item.hasRight() and not found_item.hasLeft():  # Якщо знайдений вузол має лише одну праву гілку
            found_item.setNode(found_item.rightChild())         # Замінюємо знайдений вузол його правим піддіревом

        else:  # Якщо знайдений вузол має обидві гілки
            # Знаходимо максимальний вузол у лівому піддереві вершини found_item
            nodeMax, parentMax = self.__search_max(found_item.leftChild(), found_item)
            # Замінюємо значення елемета found_item знайденим максимальним
            found_item.setNode(nodeMax.item())
            # Запускаємо рекурсивне видалення для піддерева, з вершиною nodeMax
            self.__delete_helper(nodeMax, parentMax, nodeMax.item())


def testSearchShow(item):
    found_item, parent = t.search(item)

    if found_item is None:
        print("Item = None", end=" ")
    else:
        print("Item = %s" % (found_item.item()), end=" ")

    if parent is None:
        print("Parent = None", end=" ")
    else:
        print("Parent = %d" % parent.item(), end=" ")

    print()


if __name__ == "__main__":
    t = SearchTreeWithDelete()
    # t.addNodes(10, 15, 3, 12, 122, 14, 133, 13, 1, 4, 90, 11)
    # t.addNodes(10, 3, 5, 4)


    # testSearchShow(133)
    # t.delete(90)
    # testSearchShow(90)
    # t.delete(122)
    # testSearchShow(122)

    # t.delete(14)
    #
    # testSearchShow(14)
    # testSearchShow(13)

    # t.delete(133)
    # t.delete(90)

    # t.delete(122)
    # t.delete(4)
    # t.delete(3)
    # t.delete(11)

    # print(t.searchMax())

    # t.delete(10)
    # t.delete(133)
    # t.delete(122)

    t.addItems(10, 15, 3, 12, 122, 14, 133, 13, 1, 4, 90, 11)
    # t.addNodes(10, 15, 16, 14)
    # t.addNodes(10)
    t.delete(16)
    t.delete(15)
    t.delete(14)
    t.delete(10)
    # t.addNodes(10)

    print()
