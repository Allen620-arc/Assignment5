"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import node as N


def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data values, calculate
        the sum of the data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing
                           numeric data values
    Post-condition:
            None
    Return
            :return: the sum of the data values in the node chain
    """
    if node_chain is None:
        sum_of_nodes = 0
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        sum_of_nodes = value
        # print the data
        while walker is None:
            walker = walker.get_next()
            value = walker.get_data()
            sum_of_nodes += value
            # represent the next with an arrow-like figure
        # at the end of the chain, use '/'
    return sum_of_nodes


def count_in(node_chain, value):
    """
    Purpose:
        Counts the number of times a value appears in a node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param value: a data value
    Return:
        :return: The number times the value appears in the node chain
    """
    return None


def replace_in(node_chain, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Pre-conditions:
        Each occurrence of the target value in the chain is replaced with
        the replacement value.
    Return:
        None
    """
    return None
