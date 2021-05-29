#include <stdio.h>
#include <stdlib.h>

/*
*           —трогие правила которые позвол€ют гарантировать что высота дерева O(lg(n)):
    *           1. Ћюбой узел либо черный либо красный
    *           2.  орень черный
    *           3. ¬се листь€ черные
    *           4. ¬се дети красного узла - черные
    *           5. ¬се простые пути из узла в листь€ имеют одинаковое кол-во черных узлов.
* 
            ќбщие правила :
            1) „ерна€ высота - кол - во черных узлов пути от любого узла x до листьев. (bh(x)).
            2) Ћюбой простой путь от узла - предка до листового узла - потомка содержит одинаковое число чЄрных узлов.
            3) ¬ысота дерева не превышает 2log(n + 1). < --¬от почему это хорошее дерево поискаю
            4) ѕри исправлении красно-черных свойств будет использовано не более 2-ух поворотов дерева.

            ћетоды дерева :
            1) Insert < --¬ыполн€ютс€ за O(lg(n)), могут нарушить красно - черные св - ва.
            2) Delete < --¬ыполн€ютс€ за O(lg(n)), могут нарушить красно - черные св - ва.
            3) FixInsert < --¬осстанавливает красно - черные св - ва в зависимости от сценари€(всего 5 сценариев).
            4) RotateLeft < --»змен€ют структуру указателей, сохран€ют св - ва бинарного дерева поиска.
                ”слови€: {ѕравый дочерний != NIL}
            5) RotateRight < --»змен€ют структуру указателей, сохран€ют св - ва бинарного дерева поиска.
                ”слови€: {Ћевый дочерний != NIL}
*/

enum COLOR { Red, Black };

template < typename T >
struct tree_node {
    T data;
    struct tree_node* right;
    struct tree_node* left;
    struct tree_node* parent;
    enum COLOR color;
};

template < typename T >
struct red_black_tree {
    tree_node<T>* root;
    tree_node<T>* NIL;
};


// Create new node.
template < typename T >
tree_node<T>* new_tree_node(T data) {
    tree_node<T>* n = (tree_node<T>*)malloc(sizeof(tree_node<T>));
    n->left = NULL;
    n->right = NULL;
    n->parent = NULL;
    n->data = data;
    n->color = Red;

    return n;
}


// Create new Tree.
template < typename T >
red_black_tree<T>* new_red_black_tree() {
    red_black_tree<T>* t = (red_black_tree<T>*)malloc(sizeof(red_black_tree<T>));
    tree_node<T>* nil_node = (tree_node<T>*)malloc(sizeof(tree_node<T>));
    nil_node->left = NULL;
    nil_node->right = NULL;
    nil_node->parent = NULL;
    nil_node->color = Black;
    nil_node->data = 0;
    t->NIL = nil_node;
    t->root = t->NIL;

    return t;
}

// ITERATORS -----------------------------------------------------

// Rotations --------------------------------------------------------------.
template < typename T >
void left_rotate(red_black_tree<T>* t, tree_node<T>* x) {
    tree_node<T>* y = x->right;
    x->right = y->left;
    if (y->left != t->NIL) {
        y->left->parent = x;
    }
    y->parent = x->parent;
    if (x->parent == t->NIL) { //x is root
        t->root = y;
    }
    else if (x == x->parent->left) { //x is left child
        x->parent->left = y;
    }
    else { //x is right child
        x->parent->right = y;
    }
    y->left = x;
    x->parent = y;
}

template < typename T >
void right_rotate(red_black_tree<T>* t, tree_node<T>* x) {
    tree_node<T>* y = x->left;
    x->left = y->right;
    if (y->right != t->NIL) {
        y->right->parent = x;
    }
    y->parent = x->parent;
    if (x->parent == t->NIL) { //x is root
        t->root = y;
    }
    else if (x == x->parent->right) { //x is left child
        x->parent->right = y;
    }
    else { //x is right child
        x->parent->left = y;
    }
    y->right = x;
    x->parent = y;
}


// INSERTION STUFF. -----------------------------------------------------------------------
/*
* There 6 cases.
*/
template < typename T >
void insertion_fixup(red_black_tree<T>* t, tree_node<T>* z) {
    while (z->parent->color == Red) {
        if (z->parent == z->parent->parent->left) { //z.parent is the left child (first 3 cases)

            tree_node<T>* y = z->parent->parent->right; //uncle of z (сосед его папы)

            if (y->color == Red) { //case 1 (сосед папы красный)
                z->parent->color = Black;
                y->color = Black;
                z->parent->parent->color = Red;

                // ќбновл€ем наш узел чтобы в случае чего перекрашивать и фиксить все свойства дл€ всего дерева выше.
                z = z->parent->parent;
            }
            else { //case2 or case3 (сосед папы черный)

                if (z == z->parent->right) { //case2 (наш новый узел €вл€етс€ правым потомком)
                    z = z->parent; //marked z.parent as new z
                    left_rotate(t, z);
                }
                //case3 (наш новый узел €вл€етс€ левым потомком)
                z->parent->color = Black; //made parent black
                z->parent->parent->color = Red; //made parent red
                right_rotate(t, z->parent->parent);
            }
        }
        else { //z.parent is the right child (last 3 cases)

            tree_node<T>* y = z->parent->parent->left; //uncle of z (сосед его папы)

            if (y->color == Red) {
                z->parent->color = Black;
                y->color = Black;
                z->parent->parent->color = Red;
                z = z->parent->parent;
            }
            else {
                if (z == z->parent->left) {
                    z = z->parent; //marked z.parent as new z
                    right_rotate(t, z);
                }
                z->parent->color = Black; //made parent black
                z->parent->parent->color = Red; //made parent red
                left_rotate(t, z->parent->parent);
            }
        }
    }
    t->root->color = Black;
}

template < typename T >
void insert(red_black_tree<T>* t, tree_node<T>* z) {
    tree_node<T>* y = t->NIL; // –одитель нового узла
    tree_node<T>* temp = t->root;

    // »дЄм от корн€ чтобы посмотреть куда вставл€ть.
    while (temp != t->NIL) {
        y = temp;
        if (z->data < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }
    z->parent = y;

    // —мотрим €вл€етс€ ли новый узел правым или левым от родител€.
    if (y == t->NIL) { // Ќовый узел €вл€етс€ корнем.
        t->root = z;
    }
    else if (z->data < y->data) //data of child is less than its parent, left child
        y->left = z;
    else
        y->right = z;

    z->right = t->NIL;
    z->left = t->NIL;

    // »справл€ем возможные нарушени€ свойства 2 и 4.
    insertion_fixup(t, z);
}


// Replace 'u' node to 'v' node.
template < typename T >
void rb_transplant(red_black_tree<T>* t, tree_node<T>* u, tree_node<T>* v) {
    if (u->parent == t->NIL)        // u is root.
        t->root = v;
    else if (u == u->parent->left)  // u is left child.
        u->parent->left = v;
    else                            // u is right child.
        u->parent->right = v;
    v->parent = u->parent;
}


// Returns the minimal element of Tree.
template < typename T >
tree_node<T>* minimum(red_black_tree<T>* t, tree_node<T>* x) {
    while (x->left != t->NIL)
        x = x->left;
    return x;
}


// DELETION STUFF. -----------------------------------------------------------------------
template < typename T >
void rb_delete_fixup(red_black_tree<T>* t, tree_node<T>* x) {
    while (x != t->root && x->color == Black) {
        if (x == x->parent->left) {
            tree_node<T>* w = x->parent->right;
            if (w->color == Red) {
                w->color = Black;
                x->parent->color = Red;
                left_rotate(t, x->parent);
                w = x->parent->right;
            }
            if (w->left->color == Black && w->right->color == Black) {
                w->color = Red;
                x = x->parent;
            }
            else {
                if (w->right->color == Black) {
                    w->left->color = Black;
                    w->color = Red;
                    right_rotate(t, w);
                    w = x->parent->right;
                }
                w->color = x->parent->color;
                x->parent->color = Black;
                w->right->color = Black;
                left_rotate(t, x->parent);
                x = t->root;
            }
        }
        else {
            tree_node<T>* w = x->parent->left;
            if (w->color == Red) {
                w->color = Black;
                x->parent->color = Red;
                right_rotate(t, x->parent);
                w = x->parent->left;
            }
            if (w->right->color == Black && w->left->color == Black) {
                w->color = Red;
                x = x->parent;
            }
            else {
                if (w->left->color == Black) {
                    w->right->color = Black;
                    w->color = Red;
                    left_rotate(t, w);
                    w = x->parent->left;
                }
                w->color = x->parent->color;
                x->parent->color = Black;
                w->left->color = Black;
                right_rotate(t, x->parent);
                x = t->root;
            }
        }
    }
    x->color = Black;
}

template < typename T >
void rb_delete(red_black_tree<T>* t, tree_node<T>* z) {
    tree_node<T>* y = z;
    tree_node<T>* x;
    enum COLOR y_orignal_color = y->color;
    if (z->left == t->NIL) {
        x = z->right;
        rb_transplant(t, z, z->right);
    }
    else if (z->right == t->NIL) {
        x = z->left;
        rb_transplant(t, z, z->left);
    }
    else {
        y = minimum(t, z->right);
        y_orignal_color = y->color;
        x = y->right;
        if (y->parent == z) {
            x->parent = z;
        }
        else {
            rb_transplant(t, y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        rb_transplant(t, z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    if (y_orignal_color == Black)
        rb_delete_fixup(t, x);
}


// Goes throughout all tree.
template < typename T >
void inorder(red_black_tree<T>* t, tree_node<T>* n) {
    if (n != t->NIL) {
        inorder(t, n->left);
        printf("%d\n", n->data);
        inorder(t, n->right);
    }
}


// Main logic ------------------------------------------------------------------------------
int main() {

    red_black_tree<int>* t = new_red_black_tree<int>();

    tree_node<int>* a, * b, * c, * d, * e, * f, * g, * h, * i, * j, * k, * l, * m;
    a = new_tree_node(10);
    b = new_tree_node(20);
    c = new_tree_node(30);
    d = new_tree_node(100);
    e = new_tree_node(90);
    f = new_tree_node(40);
    g = new_tree_node(50);
    h = new_tree_node(60);
    i = new_tree_node(70);
    j = new_tree_node(80);
    k = new_tree_node(150);
    l = new_tree_node(110);
    m = new_tree_node(120);

    insert(t, a);
    insert(t, b);
    insert(t, c);
    insert(t, d);
    insert(t, e);
    insert(t, f);
    insert(t, g);
    insert(t, h);
    insert(t, i);
    insert(t, j);
    insert(t, k);
    insert(t, l);
    insert(t, m);

    rb_delete(t, a);
    rb_delete(t, m);

    // Prints all nodes.
    inorder(t, t->root);

    return 0;
}
