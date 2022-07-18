package br.upf.ccc.sd.BibliotecaAlbuns.webservice;

import java.util.List;

import javax.jws.WebService;

import br.upf.ccc.sd.BibliotecaAlbuns.dao.AlbumDAO;
import br.upf.ccc.sd.BibliotecaAlbuns.model.Album;

/**
 * SIB - Service Implementation Bean 
 * É a classe que implementa a BibliotecaAlbumServer, 
 * desenvolvendo a lógica do WebService.
 */
@WebService(endpointInterface = "br.upf.ccc.sd.BibliotecaAlbuns.webservice.BibliotecaAlbunsServer")
public class BibliotecaAlbunsServerImpl implements BibliotecaAlbunsServer {

    private AlbumDAO albumDAO = new AlbumDAO();

    @Override
    public List<Album> retornaAlbuns() {    //Método que retorna os albuns da lista.
        return albumDAO.listaAlbuns();
    }

    @Override                               //Métodos que insere novos albuns.
    public void insereAlbum(String titulo, String artista, String gravadora, int ano) {
        albumDAO.insereAlbum(titulo, artista, gravadora, ano);
    }

}
