# pylint: disable=missing-docstring,invalid-name
import os
from datetime import datetime
from pathlib import Path

from botw.hashes import StockHashTable

STOCK_FILES = set(StockHashTable(True).list_stock_files()) | set(
    StockHashTable(False).list_stock_files()
)
SARC_EXTS = {
    ".sarc",
    ".pack",
    ".bactorpack",
    ".bmodelsh",
    ".beventpack",
    ".stera",
    ".stats",
    ".ssarc",
    ".spack",
    ".sbactorpack",
    ".sbmodelsh",
    ".sbeventpack",
    ".sstera",
    ".sstats",
}
AAMP_EXTS = {
    ".bxml",
    ".sbxml",
    ".bas",
    ".sbas",
    ".baglblm",
    ".sbaglblm",
    ".baglccr",
    ".sbaglccr",
    ".baglclwd",
    ".sbaglclwd",
    ".baglcube",
    ".sbaglcube",
    ".bagldof",
    ".sbagldof",
    ".baglenv",
    ".sbaglenv",
    ".baglenvset",
    ".sbaglenvset",
    ".baglfila",
    ".sbaglfila",
    ".bagllmap",
    ".sbagllmap",
    ".bagllref",
    ".sbagllref",
    ".baglmf",
    ".sbaglmf",
    ".baglshpp",
    ".sbaglshpp",
    ".baiprog",
    ".sbaiprog",
    ".baslist",
    ".sbaslist",
    ".bassetting",
    ".sbassetting",
    ".batcl",
    ".sbatcl",
    ".batcllist",
    ".sbatcllist",
    ".bawareness",
    ".sbawareness",
    ".bawntable",
    ".sbawntable",
    ".bbonectrl",
    ".sbbonectrl",
    ".bchemical",
    ".sbchemical",
    ".bchmres",
    ".sbchmres",
    ".bdemo",
    ".sbdemo",
    ".bdgnenv",
    ".sbdgnenv",
    ".bdmgparam",
    ".sbdmgparam",
    ".bdrop",
    ".sbdrop",
    ".bgapkginfo",
    ".sbgapkginfo",
    ".bgapkglist",
    ".sbgapkglist",
    ".bgenv",
    ".sbgenv",
    ".bglght",
    ".sbglght",
    ".bgmsconf",
    ".sbgmsconf",
    ".bgparamlist",
    ".sbgparamlist",
    ".bgsdw",
    ".sbgsdw",
    ".bksky",
    ".sbksky",
    ".blifecondition",
    ".sblifecondition",
    ".blod",
    ".sblod",
    ".bmodellist",
    ".sbmodellist",
    ".bmscdef",
    ".sbmscdef",
    ".bmscinfo",
    ".sbmscinfo",
    ".bnetfp",
    ".sbnetfp",
    ".bphyscharcon",
    ".sbphyscharcon",
    ".bphyscontact",
    ".sbphyscontact",
    ".bphysics",
    ".sbphysics",
    ".bphyslayer",
    ".sbphyslayer",
    ".bphysmaterial",
    ".sbphysmaterial",
    ".bphyssb",
    ".sbphyssb",
    ".bphyssubmat",
    ".sbphyssubmat",
    ".bptclconf",
    ".sbptclconf",
    ".brecipe",
    ".sbrecipe",
    ".brgbw",
    ".sbrgbw",
    ".brgcon",
    ".sbrgcon",
    ".brgconfig",
    ".sbrgconfig",
    ".brgconfiglist",
    ".sbrgconfiglist",
    ".bsfbt",
    ".sbsfbt",
    ".bsft",
    ".sbsft",
    ".bshop",
    ".sbshop",
    ".bumii",
    ".sbumii",
    ".bvege",
    ".sbvege",
    ".bactcapt",
    ".sbactcapt",
    ".bwinfo",
}
BYML_EXTS = {
    ".bgdata",
    ".sbgdata",
    ".bquestpack",
    ".sbquestpack",
    ".byml",
    ".sbyml",
    ".mubin",
    ".smubin",
    ".baischedule",
    ".sbaischedule",
    ".baniminfo",
    ".sbaniminfo",
    ".bgsvdata",
    ".sbgsvdata",
}

GAMEFILE_DIR_NAMES = {
    "Actor/Pack",
    "Pack"
}

NO_CONVERT_EXTS = {
    ".sbfres",
    ".bfres",
    ".bcamanim",
    ".sbcamanim",
    ".hkcl",
    ".hkrg",
    ".sesetlist",
    ".sbfarc",
    ".shknm2",
    ".shktmrb",
    ".bfstm",
    ".bars",
    ".sbreviewtex",
    ".sbitemico",
    ".sstats",
    ".sbstftex",
    ".sblarc",
    ".bfsar",
    ".sbmapopen",
    ".sbmaptex",
}
RSTB_EXCLUDE_EXTS = {
    ".pack",
    ".bgdata",
    ".txt",
    ".bgsvdata",
    ".yml",
    ".json",
    ".ps1",
    ".bak",
    ".bat",
    ".ini",
    ".png",
    ".bfstm",
    ".py",
    ".sh",
    ".old",
    ".stera",
}
PROFILE_RATIOS = {
    "ComplexTag": 1.58580,
    "ArmorLower": 2.77174,
    "MapConstActive": 2.62619,
    "Horse": 1.57119,
    "MapConstPassive": 3.34795,
    "Prey": 1.90845,
    "MapDynamicActive": 2.54314,
    "Anchor": 1.54027,
    "NPC": 1.75036,
    "DemoNPC": 2.44085,
    "MapDynamicPassive": 2.87003,
    "OptionalWeapon": 3.32726,
    "ArmorUpper": 2.11312,
    "ArmorHead": 2.27533,
    "Item": 2.59118,
    "WeaponBow": 2.43674,
    "Enemy": 1.70107,
    "CookResult": 1.47792,
    "HorseSaddle": 2.41971,
    "System": 1.59686,
    "WeaponShield": 2.58867,
    "MergedDungeonParts": 2.26925,
    "NoCalcActor": 1.56243,
    "SoundProxy": 1.57575,
    "WeaponSmallSword": 2.56363,
    "SiteBoss": 1.61253,
    "ActorReaction": 1.95015,
    "WeaponLargeSword": 2.40451,
    "EffectLocater": 1.68679,
    "Beam": 1.58558,
    "SoleTag": 1.60180,
    "GelEnemy": 1.69351,
    "PlayerItem": 1.82444,
    "WeaponSpear": 2.41490,
    "Bullet": 2.12249,
    "LinkTag": 1.67059,
    "ActorOption": 1.47986,
    "GiantEnemy": 1.64212,
    "EventSystem": 1.58667,
    "Dummy": 1.57355,
    "Rope": 2.45780,
    "Guardian": 2.00911,
    "Swarm": 2.29493,
    "GiantArmor": 2.74482,
    "Dragon": 1.62425,
    "GuardianComponent": 2.75823,
    "Remains": 2.23782,
    "CapturedActor": 2.33165,
    "ArmorExtra1": 3.64020,
    "AreaManagementForOthers": 1.56662,
    "SpotBgmTag": 1.54055,
    "Area": 1.57014,
    "AreaManagementForPlayer": 1.57471,
    "LineBeam": 1.58024,
    "EnvSeEmitPoint": 1.59169,
    "DemoEquipment": 2.78588,
    "SoundSystemActor": 1.66232,
    "HorseObject": 1.96967,
    "Motorcycle": 1.89353,
    "Sandworm": 1.66948,
    "GameBlanceLocater": 2.71996,
    "HorseReins": 2.78040,
    "AirWall": 1.55907,
    "NoWork": 1.55033,
    "Weapon": 2.47555,
    "SweepCollision": 1.53318,
    "ArmorExtra0": 3.24801,
    "Player": 1.44917,
    "EnemySwarm": 2.03859,
    "ArmorExtra2": 2.81442,
    "WolfLink": 1.87220,
    "PauseMenuPlayer": 1.86665,
    "LastBoss": 1.68402,
    "StaticAnchor": 1.53173,
    "EditCamera": 1.59361,
    "EventTag": 1.59889,
    "GlobalParameter": 1.55041,
    "Camera": 1.53002,
}
RSTB_EXCLUDE_NAMES = {"ActorInfo.product.byml", ".done"}
EXEC_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
NAMES = Path.home() / ".hybuild" / "names.json"


def is_in_sarc(file: Path) -> bool:
    return any(Path(p).suffix in SARC_EXTS for p in file.parts[:-1])


def get_canon_name(file: Path, allow_no_source: bool = False) -> str:
    if is_in_sarc(file):
        parent = next(reversed([p for p in file.parents if p.suffix in SARC_EXTS]))
        file = file.relative_to(parent)
        allow_no_source = True
    name = (
        file.as_posix()
        .replace("\\", "/")
        .replace("atmosphere/titles/", "")
        .replace("atmosphere/contents/", "")
        .replace("01007EF00011E000/romfs", "content")
        .replace("01007ef00011e000/romfs", "content")
        .replace("01007EF00011e000/romfs", "content")
        .replace("01007EF00011E001/romfs", "aoc/0010")
        .replace("01007EF00011e001/romfs", "aoc/0010")
        .replace("01007ef00011e001/romfs", "aoc/0010")
        .replace("01007EF00011E002/romfs", "aoc/0010")
        .replace("01007EF00011e002/romfs", "aoc/0010")
        .replace("01007ef00011E002/romfs", "aoc/0010")
        .replace("01007EF00011F001/romfs", "aoc/0010")
        .replace("01007EF00011f001/romfs", "aoc/0010")
        .replace("01007ef00011F001/romfs", "aoc/0010")
        .replace("01007EF00011F002/romfs", "aoc/0010")
        .replace("01007EF00011f002/romfs", "aoc/0010")
        .replace("01007ef00011f002/romfs", "aoc/0010")
        .replace(".s", ".")
        .replace("Content", "content")
        .replace("Aoc", "aoc")
    )
    if "aoc/" in name:
        return name.replace("aoc/content", "aoc").replace("aoc", "Aoc")
    elif "content/" in name and "/aoc" not in name:
        return name.replace("content/", "")
    elif allow_no_source:
        return name


def modified_date(self) -> datetime:
    return datetime.fromtimestamp(self.stat().st_mtime)


setattr(Path, "modified_date", modified_date)
