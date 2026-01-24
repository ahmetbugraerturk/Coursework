package exception;

/**
 * Custom runtime exception thrown when an authentication attempt is invalid.
 * 
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class InvalidAuthException extends RuntimeException {

	private static final long serialVersionUID = 1L;
	
	/**
     * Constructs a new InvalidAuthException with the specified detail message.
     *
     * @param msg the detail message explaining the reason for the exception
     */
	public InvalidAuthException(String msg) {
		super(msg);
	}

}
