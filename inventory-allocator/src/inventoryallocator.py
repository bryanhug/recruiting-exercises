#!/usr/bin/env python3
class InventoryAllocator():
	def __init__(self):
		pass
	
	def calculateShipment(self, itemsOrdered, inventoryDistribution):
		""" Compute the best way an order can be shipped
		>>> calculateShipment( { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }] )
		[{ owd: { apple: 1 } }]
		>>> calculateShipment( { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }] )
		[]
		"""
		shipments = []
		itemsLeft = itemsOrdered
		for item, numOrdered in itemsOrdered.items():
			suppliers = []
			for warehouse in inventoryDistribution:
				inventory = warehouse['inventory']
				if item in inventory and itemsLeft[item]:
					if itemsLeft[item] <= inventory[item]:
						suppliers.append({ warehouse['name']: {item: itemsLeft[item]} })
						shipments.extend(suppliers)
						itemsLeft[item] = 0
					else:
						suppliers.append({ warehouse['name']: {item: inventory[item]} })
						itemsLeft[item] = itemsLeft[item] - inventory[item] 

		# # consolidate shipments
		# for shipment in shipments:



		return shipments

