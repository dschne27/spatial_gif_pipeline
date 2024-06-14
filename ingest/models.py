from typing import Optional

from pydantic import BaseModel


class Species(BaseModel):
    '''Model for IUCN Red List Species spatial data schema.
        Mammals and Plants datasets have the same schema.'''
    id_no: Optional[int]
    sci_name: Optional[str]
    presence: Optional[int]
    origin: Optional[int]
    seasonal: Optional[int]
    compiler: Optional[int]
    yrcompiled: Optional[int]
    citation: Optional[str]
    subspecies: Optional[str]
    subpop: Optional[str]
    source: Optional[str]
    island: Optional[str]
    tax_comm: Optional[str]
    dist_comm: Optional[str]
    generalisd: Optional[int]
    legend: Optional[str]
    kingdom: Optional[str]
    phylum: Optional[str]
    class_: Optional[str]
    order_: Optional[str]
    family: Optional[str]
    genus: Optional[str]
    category: Optional[str]
    marine: Optional[str]
    terrestria: Optional[str]
    freshwater: Optional[str]
    Shape_Leng: Optional[float]
    Shape_Area: Optional[float]
    wkt: Optional[bytes]
