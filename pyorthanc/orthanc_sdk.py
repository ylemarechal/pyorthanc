try:
    from orthanc import *

except ModuleNotFoundError:
    """Orthanc SDK methods wrapped in python (plugin version 4.0)"""
    import warnings

    from typing import Any, Callable

    from ._orthanc_sdk_enums import *

    warnings.warn('Cannot import orthanc sdk. Using mock instead.')

    VERSION = '4.0'


    def AutodetectMimeType(*args):
        """Generated from C function OrthancPluginAutodetectMimeType()"""
        pass


    def BufferCompression(memory_buffer: Any,
                          source: Any,
                          size: int,
                          compression: CompressionType,
                          uncompress: int) -> int:
        """Compress or decompress a buffer.

        This function compresses or decompresses a buffer, using the version of the zlib
        library that is used by the Orthanc core.

        Parameters
        ----------
        memory_buffer
            The target memory buffer. It must be freed with OrthancPluginFreeMemoryBuffer()
        source
            The source buffer.
        size
            The size in bytes of the source buffer.
        compression
            The compression algorithm.
        uncompress
            If set to "0", the buffer must be compressed.

        Returns
        -------
            0 if success, or the error code if failure.
        """
        pass


    def CheckVersion() -> int:
        """Check the compatibility of the plugin wrt. the version of its hosting Orthanc.

        This function checks whether the version of the Orthanc server
        running this plugin, is above the version of the current Orthanc
        SDK header. This guarantees that the plugin is compatible with
        the hosting Orthanc (i.e. it will not call unavailable services).
        The result of this function should always be checked in the
        OrthancPluginInitialize() entry point of the plugin.

        Returns
        -------
            1 if and only if the versions are compatible. If the result is 0,
            the initialization of the plugin should fail.

        """
        pass


    def CheckVersionAdvanced(*args):
        """Generated from C function OrthancPluginCheckVersionAdvanced()"""
        pass


    def CompressJpegImage(*args):
        """Generated from C function OrthancPluginCompressJpegImage()"""
        pass


    def CompressPngImage(*args):
        """Generated from C function OrthancPluginCompressPngImage()"""
        pass


    def ComputeMd5(*args):
        """Generated from C function OrthancPluginComputeMd5()"""
        pass


    def ComputeSha1(*args):
        """Generated from C function OrthancPluginComputeSha1()"""
        pass


    def CreateDicom(*args):
        """None"""
        pass


    def CreateDicomInstance(*args):
        """Generated from C function OrthancPluginCreateDicomInstance()"""
        pass


    def CreateFindMatcher(*args):
        """Generated from C function OrthancPluginCreateFindMatcher()"""
        pass


    def CreateImage(*args):
        """Generated from C function OrthancPluginCreateImage()"""
        pass


    def CreateImageFromBuffer(*args):
        """None"""
        pass


    def CreateMemoryBuffer(*args):
        """Generated from C function OrthancPluginCreateMemoryBuffer()"""
        pass


    def DecodeDicomImage(*args):
        """Generated from C function OrthancPluginDecodeDicomImage()"""
        pass


    def DicomBufferToJson(*args):
        """Generated from C function OrthancPluginDicomBufferToJson()"""
        pass


    def DicomInstanceToJson(*args):
        """Generated from C function OrthancPluginDicomInstanceToJson()"""
        pass


    def ExtendOrthancExplorer(*args):
        """Generated from C function OrthancPluginExtendOrthancExplorer()"""
        pass


    def GenerateRestApiAuthorizationToken(*args):
        """Generated from C function OrthancPluginGenerateRestApiAuthorizationToken()"""
        pass


    def GenerateUuid(*args):
        """Generated from C function OrthancPluginGenerateUuid()"""
        pass


    def GetCommandLineArgument(*args):
        """Generated from C function OrthancPluginGetCommandLineArgument()"""
        pass


    def GetCommandLineArgumentsCount(*args):
        """Generated from C function OrthancPluginGetCommandLineArgumentsCount()"""
        pass


    def GetConfiguration(*args):
        """Generated from C function OrthancPluginGetConfiguration()"""
        pass


    def GetConfigurationPath(*args):
        """Generated from C function OrthancPluginGetConfigurationPath()"""
        pass


    def GetDicomForInstance(*args):
        """Generated from C function OrthancPluginGetDicomForInstance()"""
        pass


    def GetErrorDescription(*args):
        """Generated from C function OrthancPluginGetErrorDescription()"""
        pass


    def GetExpectedDatabaseVersion(*args):
        """Generated from C function OrthancPluginGetExpectedDatabaseVersion()"""
        pass


    def GetFontName(*args):
        """Generated from C function OrthancPluginGetFontName()"""
        pass


    def GetFontSize(*args):
        """Generated from C function OrthancPluginGetFontSize()"""
        pass


    def GetFontsCount(*args):
        """Generated from C function OrthancPluginGetFontsCount()"""
        pass


    def GetGlobalProperty(*args):
        """Generated from C function OrthancPluginGetGlobalProperty()"""
        pass


    def GetOrthancDirectory(*args):
        """Generated from C function OrthancPluginGetOrthancDirectory()"""
        pass


    def GetOrthancPath(*args):
        """Generated from C function OrthancPluginGetOrthancPath()"""
        pass


    def GetPeers(*args):
        """Generated from C function OrthancPluginGetPeers()"""
        pass


    def GetTagName(*args):
        """Generated from C function OrthancPluginGetTagName()"""
        pass


    def HttpDelete(*args):
        """Generated from C function OrthancPluginHttpDelete()"""
        pass


    def HttpGet(*args):
        """Generated from C function OrthancPluginHttpGet()"""
        pass


    def HttpPost(*args):
        """Generated from C function OrthancPluginHttpPost()"""
        pass


    def HttpPut(*args):
        """Generated from C function OrthancPluginHttpPut()"""
        pass


    def LogError(*args):
        """Generated from C function OrthancPluginLogError()"""
        pass


    def LogInfo(*args):
        """Generated from C function OrthancPluginLogInfo()"""
        pass


    def LogWarning(*args):
        """Generated from C function OrthancPluginLogWarning()"""
        pass


    def LookupDictionary(*args):
        """None"""
        pass


    def LookupInstance(*args):
        """Generated from C function OrthancPluginLookupInstance()"""
        pass


    def LookupPatient(*args):
        """Generated from C function OrthancPluginLookupPatient()"""
        pass


    def LookupSeries(*args):
        """Generated from C function OrthancPluginLookupSeries()"""
        pass


    def LookupStudy(*args):
        """Generated from C function OrthancPluginLookupStudy()"""
        pass


    def LookupStudyWithAccessionNumber(*args):
        """Generated from C function OrthancPluginLookupStudyWithAccessionNumber()"""
        pass


    def ReadFile(*args):
        """Generated from C function OrthancPluginReadFile()"""
        pass


    def RegisterDictionaryTag(*args):
        """Generated from C function OrthancPluginRegisterDictionaryTag()"""
        pass


    def RegisterErrorCode(*args):
        """Generated from C function OrthancPluginRegisterErrorCode()"""
        pass


    def RegisterFindCallback(*args):
        """None"""
        pass


    def RegisterIncomingCStoreInstanceFilter(*args):
        """None"""
        pass


    def RegisterIncomingHttpRequestFilter(*args):
        """None"""
        pass


    def RegisterMoveCallback(*args):
        """None"""
        pass


    def RegisterOnChangeCallback(*args):
        """None"""
        pass


    def RegisterOnStoredInstanceCallback(*args):
        """None"""
        pass


    def RegisterPrivateDictionaryTag(*args):
        """Generated from C function OrthancPluginRegisterPrivateDictionaryTag()"""
        pass


    def RegisterReceivedInstanceCallback(*args):
        """None"""
        pass


    def RegisterRestCallback(new_route: str, callback: Callable) -> None:
        """Register a REST callback.

        This function registers a REST callback against a regular
        expression for a URI. This function must be called during the
        initialization of the plugin, i.e. inside the
        OrthancPluginInitialize() public function.

        Parameters
        ----------
        new_route
            Regular expression for the URI. May contain groups.
        callback
            The callback function to handle the REST call.

        Examples
        --------
        ```python
        def on_rest(output, uri, **request):
            print(request)


        orthanc.RegisterRestCallback('/tata', on_rest)
        ```
        """
        pass


    def RegisterStorageArea(*args):
        """None"""
        pass


    def RegisterStorageCommitmentScpCallback(*args):
        """None"""
        pass


    def RegisterWorklistCallback(*args):
        """None"""
        pass


    def RestApiDelete(*args):
        """Generated from C function OrthancPluginRestApiDelete()"""
        pass


    def RestApiDeleteAfterPlugins(*args):
        """Generated from C function OrthancPluginRestApiDeleteAfterPlugins()"""
        pass


    def RestApiGet(*args):
        """Generated from C function OrthancPluginRestApiGet()"""
        pass


    def RestApiGetAfterPlugins(*args):
        """Generated from C function OrthancPluginRestApiGetAfterPlugins()"""
        pass


    def RestApiPost(uri: str, body: Any, *args, **kwargs):
        """Make a POST call to the built-in Orthanc REST API.

        Make a POST call to the built-in Orthanc REST API. The result to
        the query is stored into a newly allocated memory buffer.

        Parameters
        ----------
        uri
            The URI in the built-in Orthanc API.
        body
            The body of the POST request.
        *args
        **kwargs

        """
        pass


    def RestApiPostAfterPlugins(*args):
        """Generated from C function OrthancPluginRestApiPostAfterPlugins()"""
        pass


    def RestApiPut(*args):
        """Generated from C function OrthancPluginRestApiPut()"""
        pass


    def RestApiPutAfterPlugins(*args):
        """Generated from C function OrthancPluginRestApiPutAfterPlugins()"""
        pass


    def SetDescription(*args):
        """Generated from C function OrthancPluginSetDescription()"""
        pass


    def SetGlobalProperty(*args):
        """Generated from C function OrthancPluginSetGlobalProperty()"""
        pass


    def SetMetricsValue(*args):
        """Generated from C function OrthancPluginSetMetricsValue()"""
        pass


    def SetRootUri(*args):
        """Generated from C function OrthancPluginSetRootUri()"""
        pass


    def TranscodeDicomInstance(*args):
        """Generated from C function OrthancPluginTranscodeDicomInstance()"""
        pass


    def UncompressImage(*args):
        """Generated from C function OrthancPluginUncompressImage()"""
        pass


    def WriteFile(*args):
        """Generated from C function OrthancPluginWriteFile()"""
        pass


    class DicomInstance:
        """Generated from Orthanc C class: OrthancPluginDicomInstance"""

        def GetInstanceAdvancedJson(self, *args):
            """Generated from C function OrthancPluginGetInstanceAdvancedJson()"""
            pass

        def GetInstanceData(self, *args):
            """Generated from C function OrthancPluginGetInstanceData()"""
            pass

        def GetInstanceDecodedFrame(self, *args):
            """Generated from C function OrthancPluginGetInstanceDecodedFrame()"""
            pass

        def GetInstanceFramesCount(self, *args):
            """Generated from C function OrthancPluginGetInstanceFramesCount()"""
            pass

        def GetInstanceJson(self, *args):
            """Generated from C function OrthancPluginGetInstanceJson()"""
            pass

        def GetInstanceMetadata(self, *args):
            """Generated from C function OrthancPluginGetInstanceMetadata()"""
            pass

        def GetInstanceOrigin(self, *args):
            """Generated from C function OrthancPluginGetInstanceOrigin()"""
            pass

        def GetInstanceRawFrame(self, *args):
            """Generated from C function OrthancPluginGetInstanceRawFrame()"""
            pass

        def GetInstanceRemoteAet(self, *args):
            """Generated from C function OrthancPluginGetInstanceRemoteAet()"""
            pass

        def GetInstanceSimplifiedJson(self, *args):
            """Generated from C function OrthancPluginGetInstanceSimplifiedJson()"""
            pass

        def GetInstanceSize(self, *args):
            """Generated from C function OrthancPluginGetInstanceSize()"""
            pass

        def GetInstanceTransferSyntaxUid(self, *args):
            """Generated from C function OrthancPluginGetInstanceTransferSyntaxUid()"""
            pass

        def HasInstanceMetadata(self, *args):
            """Generated from C function OrthancPluginHasInstanceMetadata()"""
            pass

        def HasInstancePixelData(self, *args):
            """Generated from C function OrthancPluginHasInstancePixelData()"""
            pass

        def SerializeDicomInstance(self, *args):
            """Generated from C function OrthancPluginSerializeDicomInstance()"""
            pass


    class FindAnswers:
        """Generated from Orthanc C class: OrthancPluginFindAnswers"""

        def FindAddAnswer(self, *args):
            """Generated from C function OrthancPluginFindAddAnswer()"""
            pass

        def FindMarkIncomplete(self, *args):
            """Generated from C function OrthancPluginFindMarkIncomplete()"""
            pass


    class FindMatcher:
        """Generated from Orthanc C class: OrthancPluginFindMatcher"""

        def FindMatcherIsMatch(self, *args):
            """Generated from C function OrthancPluginFindMatcherIsMatch()"""
            pass


    class FindQuery:
        """Generated from Orthanc C class: OrthancPluginFindQuery"""

        def GetFindQuerySize(self, *args):
            """Generated from C function OrthancPluginGetFindQuerySize()"""
            pass

        def GetFindQueryTagElement(self, *args):
            """Generated from C function OrthancPluginGetFindQueryTag()"""
            pass

        def GetFindQueryTagGroup(self, *args):
            """Generated from C function OrthancPluginGetFindQueryTag()"""
            pass

        def GetFindQueryTagName(self, *args):
            """Generated from C function OrthancPluginGetFindQueryTagName()"""
            pass

        def GetFindQueryValue(self, *args):
            """Generated from C function OrthancPluginGetFindQueryValue()"""
            pass


    class Image:
        """Generated from Orthanc C class: OrthancPluginImage"""

        def ConvertPixelFormat(self, *args):
            """Generated from C function OrthancPluginConvertPixelFormat()"""
            pass

        def DrawText(self, *args):
            """Generated from C function OrthancPluginDrawText()"""
            pass

        def GetImageBuffer(self, *args):
            """Generated from C function OrthancPluginGetImageBuffer()"""
            pass

        def GetImageHeight(self, *args):
            """Generated from C function OrthancPluginGetImageHeight()"""
            pass

        def GetImagePitch(self, *args):
            """Generated from C function OrthancPluginGetImagePitch()"""
            pass

        def GetImagePixelFormat(self, *args):
            """Generated from C function OrthancPluginGetImagePixelFormat()"""
            pass

        def GetImageWidth(self, *args):
            """Generated from C function OrthancPluginGetImageWidth()"""
            pass


    class Job:
        """Generated from Orthanc C class: OrthancPluginJob"""

        def SubmitJob(self, *args):
            """Generated from C function OrthancPluginSubmitJob()"""
            pass


    class OrthancException:
        """Common base class for all non-exit exceptions."""

        def with_traceback(self, *args):
            """Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self."""
            pass


    class Peers:
        """Generated from Orthanc C class: OrthancPluginPeers"""

        def GetPeerName(self, *args):
            """Generated from C function OrthancPluginGetPeerName()"""
            pass

        def GetPeerUrl(self, *args):
            """Generated from C function OrthancPluginGetPeerUrl()"""
            pass

        def GetPeerUserProperty(self, *args):
            """Generated from C function OrthancPluginGetPeerUserProperty()"""
            pass

        def GetPeersCount(self, *args):
            """Generated from C function OrthancPluginGetPeersCount()"""
            pass


    class RestOutput:
        """Generated from Orthanc C class: OrthancPluginRestOutput"""

        def AnswerBuffer(self, *args):
            """Generated from C function OrthancPluginAnswerBuffer()"""
            pass

        def CompressAndAnswerJpegImage(self, *args):
            """Generated from C function OrthancPluginCompressAndAnswerJpegImage()"""
            pass

        def CompressAndAnswerPngImage(self, *args):
            """Generated from C function OrthancPluginCompressAndAnswerPngImage()"""
            pass

        def Redirect(self, *args):
            """Generated from C function OrthancPluginRedirect()"""
            pass

        def SendHttpStatus(self, *args):
            """Generated from C function OrthancPluginSendHttpStatus()"""
            pass

        def SendHttpStatusCode(self, *args):
            """Generated from C function OrthancPluginSendHttpStatusCode()"""
            pass

        def SendMethodNotAllowed(self, *args):
            """Generated from C function OrthancPluginSendMethodNotAllowed()"""
            pass

        def SendMultipartItem(self, *args):
            """Generated from C function OrthancPluginSendMultipartItem()"""
            pass

        def SendUnauthorized(self, *args):
            """Generated from C function OrthancPluginSendUnauthorized()"""
            pass

        def SetCookie(self, *args):
            """Generated from C function OrthancPluginSetCookie()"""
            pass

        def SetHttpErrorDetails(self, *args):
            """Generated from C function OrthancPluginSetHttpErrorDetails()"""
            pass

        def SetHttpHeader(self, *args):
            """Generated from C function OrthancPluginSetHttpHeader()"""
            pass

        def StartMultipartAnswer(self, *args):
            """Generated from C function OrthancPluginStartMultipartAnswer()"""
            pass


    class ServerChunkedRequestReader:
        """Generated from Orthanc C class: OrthancPluginServerChunkedRequestReader"""


    class StorageArea:
        """Generated from Orthanc C class: OrthancPluginStorageArea"""

        def ReconstructMainDicomTags(self, *args):
            """Generated from C function OrthancPluginReconstructMainDicomTags()"""
            pass

        def StorageAreaCreate(self, *args):
            """Generated from C function OrthancPluginStorageAreaCreate()"""
            pass

        def StorageAreaRead(self, *args):
            """Generated from C function OrthancPluginStorageAreaRead()"""
            pass

        def StorageAreaRemove(self, *args):
            """Generated from C function OrthancPluginStorageAreaRemove()"""
            pass


    class WorklistAnswers:
        """Generated from Orthanc C class: OrthancPluginWorklistAnswers"""

        def WorklistAddAnswer(self, *args):
            """Generated from C function OrthancPluginWorklistAddAnswer()"""
            pass

        def WorklistMarkIncomplete(self, *args):
            """Generated from C function OrthancPluginWorklistMarkIncomplete()"""
            pass


    class WorklistQuery:
        """Generated from Orthanc C class: OrthancPluginWorklistQuery"""

        def WorklistGetDicomQuery(self, *args):
            """Generated from C function OrthancPluginWorklistGetDicomQuery()"""
            pass

        def WorklistIsMatch(self, *args):
            """Generated from C function OrthancPluginWorklistIsMatch()"""
            pass


    class __loader__:
        """Meta path import for built-in modules."""
