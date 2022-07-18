package br.upf.ccc.sd.BibliotecaAlbuns;

import javax.xml.ws.Endpoint;

import br.upf.ccc.sd.BibliotecaAlbuns.webservice.BibliotecaAlbunsServerImpl;

//Publisher: Publica a implementação de um WebService
 
public class BibliotecaAlbunsPublisher {

    public static void main(String[] args) {
        Endpoint.publish("http://localhost:4848/biblioteca", new BibliotecaAlbunsServerImpl());
    }
}
