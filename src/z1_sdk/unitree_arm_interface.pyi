import numpy as np
from enum import IntEnum

def postureToHomo(posture: np.ndarray, /) -> np.ndarray: ...

def homoToPosture(T: np.ndarray, /) -> np.ndarray: ...

class ArmFSMState(IntEnum):
    INVALID = 0,
    PASSIVE = 1,
    JOINTCTRL = 2,
    CARTESIAN = 3,
    MOVEJ = 4,
    MOVEL = 5,
    MOVEC = 6,
    TEACH = 7,
    TEACHREPEAT = 8,
    TOSTATE = 9,
    SAVESTATE = 10,
    TRAJECTORY = 11,
    LOWCMD = 12

class LowlevelState:
    def getQ(self) -> np.array: ...

    def getQd(self) -> np.array: ...
    
    def getTau(self) -> np.array: ...

    def getGripperQ(self) -> np.array: ...

class CtrlComponents:
    @property
    def armModel(self) -> Z1Model: ...
    
    @property
    def dt(self) -> float: ...

class Z1Model:
    def __init__(self, endPosLocal: np.array, endEffectorMass: float, endEffectorCom: np.array, endEffectorInertia: np.ndarray, /): ...

    def checkInSingularity(self, q: np.array, /) -> bool: ...

    def forwardKinematics(self, q: np.array, index, /) -> np.ndarray: ...

    def inverseKinematics(self, Tdes: np.ndarray, qPast: np.array, checkInWrokSpace: bool, /) -> bool: ...

    def solveQP(self, twist: np.array, qPast: np.array, dt: float, /): ...

    def CalcJacobian(self, q: np.array, /) -> np.ndarray: ...

    def inverseDynamics(self, q: np.array, qd: np.array, qdd: np.array, Ftip: np.array, /) -> np.array: ...

    def jointProtect(self, q: np.array, qd: np.array, /): ...

    def getJointQMax(self) -> np.array: ...

    def getJointQMin(self) -> np.array: ...

    def getJointSpeedMax(self) -> np.array: ...

class ArmInterface:
    def __init__(self, hasGripper: bool, /) -> None: ...

    def setFsm(self, fsm: ArmFSMState): ...

    def setFsmLowcmd(self): ...

    def getCurrentState(self) -> ArmFSMState: ...

    def loopOn(self): ...
    
    def loopOff(self): ...

    def backToStart(self): ...

    def labelRun(self, label: str, /): ...

    def labelSave(self, label: str, /): ...

    def teach(self, label: str, /): ...

    def teachRepeat(self, label: str, /): ...

    def calibration(self): ...

    def MoveJ(self, posture: np.ndarray, maxSpeed: float, /) -> bool: ...

    def MoveJ(self, posture: np.ndarray, gripperPos: float, maxSpeed: float, /) -> bool: ...

    def MoveL(self, posture: np.ndarray, maxSpeed: float, /) -> bool: ...

    def MoveL(self, posture: np.ndarray, gripperPos: float, maxSpeed: float, /) -> bool: ...

    def MoveC(self, middlePosture: np.ndarray, endPosture: np.ndarray, maxSpeed: float, /) -> bool: ...

    def MoveC(self, middlePosture: np.ndarray, endPosture: np.ndarray, gripperPos: float, maxSpeed: float, /) -> bool: ...

    def startTrack(self, fsm: ArmFSMState, /): ...

    def sendRecv(self): ...

    def setWait(self, Y_N: bool, /): ...

    def jointCtrlCmd(self, directions: np.ndarray, jointSpeed: float, /): ...

    def cartesianCtrlCmd(self, directions: np.ndarray, oriSpeed: float, posSpeed: float, /): ...

    def setArmCmd(self, q: np.ndarray, qd: np.ndarray, tau: np.ndarray, /): ...

    def setGripperCmd(self, gripperPos: float, gripperW: float, gripperTau: float, /): ...

    @property
    def lowstate(self) -> LowlevelState: ...

    @property
    def _ctrlComp(self) -> CtrlComponents: ...

    @property
    def q(self) -> np.array: ...

    @property
    def qd(self) -> np.array: ...

    @property
    def tau(self) -> np.array: ...

    @property
    def gripperQ(self) -> float: ...

    @property
    def gripperQd(self) -> float: ...

    @property
    def gripperTau(self) -> float: ...