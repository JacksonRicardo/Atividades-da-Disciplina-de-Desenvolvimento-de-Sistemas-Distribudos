package br.upf.ccc.sd.BibliotecaAlbuns.webservice;

import java.util.List;

import javax.jws.WebService;
import javax.jws.WebMethod;

import br.upf.ccc.sd.BibliotecaAlbuns.model.Album;

 //SEI - Service Endpoint Interface
@WebService   //Notação WebService
public interface BibliotecaAlbunsServer {
	
	/** Métodos do WebService **/
	@WebMethod
	public List<Album> retornaAlbuns();
	
	@WebMethod
	public void insereAlbum(String titulo, String artista, String gravadora, int ano);
}