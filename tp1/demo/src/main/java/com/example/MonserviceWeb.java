package com.example;
//Soap:simple object access Protocol
//JAX-WS (JAVA ANNOTATION XML for Web Services )
//JAXB (JAVA ANNOTATION XML Building)


//URL : Uniforme Resorce Locator
//URN Uniforme Resorce Name

import javax.jws.WebService;
import javax.servlet.annotation.WebServlet;
@WebServlet(targetNamespace="")
public class MonserviceWeb {
    public double conversion(double mt) {
        return mt * 0.9;
    }
}
