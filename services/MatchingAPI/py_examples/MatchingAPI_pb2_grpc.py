# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import MatchingAPI_pb2 as MatchingAPI__pb2


class MatchApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getKP = channel.unary_unary(
        '/MatchingApi.MatchApi/getKP',
        request_serializer=MatchingAPI__pb2.keypointRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.keypointResponse.FromString,
        )
    self.getDescByImage = channel.unary_unary(
        '/MatchingApi.MatchApi/getDescByImage',
        request_serializer=MatchingAPI__pb2.descriptorRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.descriptorResponse.FromString,
        )
    self.getDescByKps = channel.unary_unary(
        '/MatchingApi.MatchApi/getDescByKps',
        request_serializer=MatchingAPI__pb2.descriptorByKpsRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.descriptorResponse.FromString,
        )
    self.getMatch = channel.unary_unary(
        '/MatchingApi.MatchApi/getMatch',
        request_serializer=MatchingAPI__pb2.matchingRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.matchingResponse.FromString,
        )
    self.getMatchByImage = channel.unary_unary(
        '/MatchingApi.MatchApi/getMatchByImage',
        request_serializer=MatchingAPI__pb2.matchingByImageRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.matchingByImageResponse.FromString,
        )
    self.getTransformParameters = channel.unary_unary(
        '/MatchingApi.MatchApi/getTransformParameters',
        request_serializer=MatchingAPI__pb2.transformRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.transformResponse.FromString,
        )
    self.getTransformParametersByImage = channel.unary_unary(
        '/MatchingApi.MatchApi/getTransformParametersByImage',
        request_serializer=MatchingAPI__pb2.transformByImageRequest.SerializeToString,
        response_deserializer=MatchingAPI__pb2.transformResponse.FromString,
        )


class MatchApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getKP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDescByImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDescByKps(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMatchByImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTransformParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTransformParametersByImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MatchApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getKP': grpc.unary_unary_rpc_method_handler(
          servicer.getKP,
          request_deserializer=MatchingAPI__pb2.keypointRequest.FromString,
          response_serializer=MatchingAPI__pb2.keypointResponse.SerializeToString,
      ),
      'getDescByImage': grpc.unary_unary_rpc_method_handler(
          servicer.getDescByImage,
          request_deserializer=MatchingAPI__pb2.descriptorRequest.FromString,
          response_serializer=MatchingAPI__pb2.descriptorResponse.SerializeToString,
      ),
      'getDescByKps': grpc.unary_unary_rpc_method_handler(
          servicer.getDescByKps,
          request_deserializer=MatchingAPI__pb2.descriptorByKpsRequest.FromString,
          response_serializer=MatchingAPI__pb2.descriptorResponse.SerializeToString,
      ),
      'getMatch': grpc.unary_unary_rpc_method_handler(
          servicer.getMatch,
          request_deserializer=MatchingAPI__pb2.matchingRequest.FromString,
          response_serializer=MatchingAPI__pb2.matchingResponse.SerializeToString,
      ),
      'getMatchByImage': grpc.unary_unary_rpc_method_handler(
          servicer.getMatchByImage,
          request_deserializer=MatchingAPI__pb2.matchingByImageRequest.FromString,
          response_serializer=MatchingAPI__pb2.matchingByImageResponse.SerializeToString,
      ),
      'getTransformParameters': grpc.unary_unary_rpc_method_handler(
          servicer.getTransformParameters,
          request_deserializer=MatchingAPI__pb2.transformRequest.FromString,
          response_serializer=MatchingAPI__pb2.transformResponse.SerializeToString,
      ),
      'getTransformParametersByImage': grpc.unary_unary_rpc_method_handler(
          servicer.getTransformParametersByImage,
          request_deserializer=MatchingAPI__pb2.transformByImageRequest.FromString,
          response_serializer=MatchingAPI__pb2.transformResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MatchingApi.MatchApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))