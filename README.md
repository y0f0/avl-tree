# avl-tree

---

## Tree Methods

* next(value) -> Node <==> минимальный элемент в дереве, строго больший value
* prev(value) -> Node <==> максимальный элемент в дереве, строго меньший value
* exists(value) -> bool <==> есть ли ключ value в дереве или нет
* insert(value) <==> добавить в дерево ключ value
* delete(value) <==> удалить ключ value
* inorder_from_root() <==> вывод всех ключей в порядке inorder
* to_list_from_root() -> List <==>  списко всех ключей в порядке inorder
