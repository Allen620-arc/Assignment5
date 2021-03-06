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
        sum_of_values = 0
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        sum_of_values = value
        while walker is not None:
            walker = walker.get_next()
            if walker is None:
                break
            else:
                value = walker.get_data()
                sum_of_values += value
    return sum_of_values


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
    num_count = 0
    if node_chain is None:
        num_count = 0
    else:
        # walk along the chain
        walker = node_chain
        while walker is not None:
            if walker.get_data() == value:
                num_count += 1
                walker = walker.get_next()
            else:
                walker = walker.get_next()
    return num_count


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
    # walk along the chain
    if node_chain is None:
        return "EMPTY"
    else:
        walker = node_chain
        while walker is not None:
            if walker.get_data() == target:
                walker.set_data(replacement)
            walker = walker.get_next()
    return None
