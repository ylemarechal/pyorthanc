from typing import Dict, List, Optional

from ..client import Orthanc


class Resource:

    def __init__(self, id_: str, client: Orthanc, lock: bool = False) -> None:
        """Constructor

        Parameters
        ----------
        id_
            Orthanc identifier of the resource
        client
            Orthanc client
        lock
            Specify if the Resource state should be locked. This is useful when the child resources
            have been filtered out, and you don't want the resource to return an updated version
            or all of those children. "lock=True" is notably used for the "find" function,
            so that only the filtered resources are kept.
        """
        self.id_ = id_
        self.client = client

        self.lock = lock
        self._information: Optional[Dict] = None
        self._child_resources: Optional[List['Resource']] = None

    @property
    def identifier(self) -> str:
        """Get Orthanc's identifier

        Returns
        -------
        str
            Resource's identifier
        """
        return self.id_

    def __eq__(self, other: 'Resource') -> bool:
        return self.id_ == other.id_
