from src import inventoryallocator as test

import pytest

inst = test.InventoryAllocator()

def checkEqual(L1, L2):
    return ( ([i for i in L1 if i not in L2] + [j for j in L2 if j not in L1]) == [])

def test_split():
    item_map = { 'apple': 10 }
    warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
    expected = [{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5 } }]
    output = inst.calculateShipment(item_map, warehouses)
    assert(checkEqual(expected,output))
    print('test_split passed!')

def test_empty():
    assert (inst.calculateShipment( { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]) == [])
    print('test_empty passed!')

def test_happy_case():
    item_map = { 'apple': 1 }
    warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
    expected = [{ 'owd': { 'apple': 1 } }]
    output = inst.calculateShipment(item_map, warehouses)
    assert (checkEqual(expected,output))
    print('test_happy_case passed!')

def test_cheapest_factory():
    item_map = { 'apple': 5, 'banana': 5, 'orange': 5 }
    warehouses = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]
    output = inst.calculateShipment(item_map, warehouses)
    expected = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}]
    print(output)
    assert(checkEqual(expected,output))
    print('test_cheapest_factory passed!')

def test_ship_one_factory():
    pass


