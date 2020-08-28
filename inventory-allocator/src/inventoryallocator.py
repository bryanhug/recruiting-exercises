#!/usr/bin/env python3
class InventoryAllocator():
	def __init__(self):
		pass
	
	def consolidateShipments(self, shipments):
		suppliers_dict = {}
		for order in shipments:
			for key,value in order.items():
				if key in suppliers_dict:
					suppliers_dict[key].update(value)
				else:
					suppliers_dict[key] = value
		return [{k:v} for k,v in suppliers_dict.items()]
	
	def calculateShipment(self, itemsOrdered, inventoryDistribution):
		""" Compute the best way an order can be shipped
		>>> calculateShipment( { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }] )
		[{ owd: { apple: 1 } }]
		>>> calculateShipment( { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }] )
		[]
		"""
		shipments = []
		itemsLeft = itemsOrdered.copy()
		for item in itemsOrdered.keys():
			suppliers = []
			for warehouse in inventoryDistribution:
				inventory = warehouse['inventory']
				name = warehouse['name']
				#check if warehouse can satisfy whole shipment
				x = [{name: {k:v}} for k,v in itemsOrdered.items() if k in inventory.keys() and v <= inventory[k]]
				if len(x) == len(itemsOrdered.keys()):
					#check if they can do all orders
					return self.consolidateShipments(x)
					# pass

				if item in inventory and itemsLeft[item]:
					if itemsLeft[item] <= inventory[item]:
						suppliers.append({ name: {item: itemsLeft[item]} })
						shipments.extend(suppliers)
						itemsLeft[item] = 0
					else:
						suppliers.append({ name: {item: inventory[item]} })
						itemsLeft[item] = itemsLeft[item] - inventory[item] 

		return self.consolidateShipments(shipments)

