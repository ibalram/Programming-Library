

# Enums and Constants
# --------------------
from enum import Enum
class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = range(1,6)

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = range(1,7)

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = range(1,4)

class Address:
    def __init__(self, street, city, state, zipCode, country):
        self._street = street
        self._city  = city
        self._state = state
        self._zipCode = zipCode

class Person:
    def __init__(self, name, address, email, phone):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
















# ParkingSpot
# -----------

# Abstract
class ParkingSpot:
    def __init__(self, number: str, parkingSpotType: ParkingSpotType):
        self._number = number
        self._parkingSpotType = parkingSpotType
        self._free = True
        self._vehicle = None

    def assignVehicle(self, vehicle: Vehicle) -> bool:
        self._vehicle = vehicle
        self.free = False
        pass

    def removeVehicle(self) -> bool:
        self._vehicle = None
        self.free = True
        pass

    def isFree(self) -> bool:
        return self._free

class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkignSpotType.HANDICAPPED)

class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)

class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)

class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)

class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)



# Vehicle
# -------
from abc import ABC
class Vehicle(ABC):
    def __init__(self, licenseNumber: str, vehicleType: VehicleType, ticket: ParkingTicket = None):
        self._licenseNumber = licenseNumber
        self._vehicleType = vehicleType
        self._ticket = ticket

    def assignTicket(self, ticket):
        self._ticket = ticket

class Car(Vehicle):
    def __init__(self, licenseNumber: str, ticket: ParkingTicket = None):
        super().__init__(licenseNumber, VehicleType.CAR, ticket)

class Van(Vehicle):
    def __init__(self, licenseNumber: str, ticket: ParkingTicket = None):
        super().__init__(licenseNumber, VehicleType.VAN, ticket)

class Truck(Vehicle):
    def __init__(self, licenseNumber: str, ticket: ParkingTicket = None):
        super().__init__(licenseNumber, VehicleType.TRUCK, ticket)

class MotorCycle(Vehicle):
    def __init__(self, licenseNumber: str, ticket: ParkingTicket = None):
        super().__init__(licenseNumber, VehicleType.MOTORBIKE, ticket)

class Electric(Vehicle):
    def __init__(self, licenseNumber: str, ticket: ParkingTicket = None):
        super().__init__(licenseNumber, VehicleType.ELECTRIC, ticket)





# ParkingFloor
# ------------

class ParkingFloor:
    def __init__(self, name: str):
        self._name = name
        self._handicappedSpots = {}
        self._compactSpots = {}
        self._largeSpots = {}
        self._electricSpots = {}
        self._infoPortals = {}
        self.switcher = {
            ParkingSpot.HANDICAPPED: self._handicappedSpots,
            ParkingSpot.COMPACT: self._compactSpots,
            ParkingSpot.LARGE: self._largeSpots,
            ParkingSpot.ELECTRIC: self._electricSpots
        }
        self.freeSpotCounts = {
            ParkingSpot.HANDICAPPED: 0,
            ParkingSpot.COMPACT: 0,
            ParkingSpot.LARGE: 0,
            ParkingSpot.ELECTRIC: 0
        }
        self._parkingDisplayBoard = ParkingDisplayBoard()

    def addParkingSpot(self, spot: ParkingSpot) -> bool:
        if spot.getType() in self.switcher:
            self.switcher[spot.getType()][spot.getNumber()] = spot
            return True
        return False

    def assignVehicleToSpot(self, vehicle, spot):
        if spot.getType() in self.switcher:
            spot.assignVehicle(vehicle)
            # self.switcher[spot.getType()] =
            self.updateParkingDisplayBoard(spot)
            return True
        return False

    def updateParkingDisplayBoard(self, spot):
        if self._parkingDisplayBoard.getFreeSpot(spot.getType()).getNumber()==spot.getNumber():
            for spotNumber, spotInstance in self.switcher[spot.getType()].items():
                if spotInstance.isFree():
                    self._parkingDisplayBoard.setFreeSpot(spotInstance)
                    break
            self._parkingDisplayBoard.showFreeSpotNumbers()

    def freeSpot(self, spot):
        spot.removeVehicle()
        self.freeSpotCounts[spot.getType()]+=1



# ParkignDisplayBoard

class ParkingDisplayBoard:
    def __init__(self, id=1):
        self._id = id
        self._freeSpot = {
            ParkingSpot.HANDICAPPED: None,
            ParkingSpot.COMPACT: None,
            ParkingSpot.LARGE: None,
            ParkingSpot.ELECTRIC: None
        }

    def showEmptySpotNumber(self):
        message = ""
        for spotType, emptySpot in self._freeSpot.items():
            if emptySpot is None:
                message += spotType.name + "is full\n"
            else:
                message += "Free "+spotType.name+": "+emptySpot.getNumber()+"\n"
        print(message)














# Account, Admin and ParkingAttendant
# -----------------------------------

# Abstract class for Admin and ParkignAttendant
class Account:
    def __init__(self, userName, password, person, status = AccountStatus.ACTIVE):
        self._userName = userName
        self._password = password
        self._person = person
        self._status = status

    def resetPassword(self):
        pass

class Admin(Account):
    def __init__(self, userName, password, person, status = AccountStatus.ACTIVE):
        super().__init(userName, password, person, status)

    def addParkingFloor(self, floor: ParkingFloor):
        pass

    def addParkingSpot(self, floorName: str, spot: ParkingSpot) -> None:
        pass

    def addParkingAttendant(self, parkingAttendant: ParkingAttendant) -> None:
        pass

    def addParkingDisplayBoard(self, floorName: String, displayBoard: DisplayBoard) -> None:
        pass

    def addEntrancePanel(self, entrancePanel: EntrancePanel) -> None:
        pass

    def addExitPanel(self, exitPanel: ExitPanel) -> None:
        pass


class ParkingAttendant(Account):
    def __init__(self, userName, password, person, status = AccountStatus.Active):
        super().__init__(userName, password, person, status)

    def processTicket(self, ticketNumber: int) -> bool:
        pass
