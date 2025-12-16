from transport_factory import TransportFactory

factory = TransportFactory()
transport = factory.create_transport("bike")
transport.drive()
