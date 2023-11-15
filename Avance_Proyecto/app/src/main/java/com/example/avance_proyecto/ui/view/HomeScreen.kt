package com.example.avance_proyecto.ui.view

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Button
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.compose.rememberNavController
import com.example.avance_proyecto.navigation.AppScreen
import com.example.avance_proyecto.ui.theme.Avance_ProyectoTheme

@Composable
fun HomeScreen(navController: NavController){
    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "CONDOSA",
                        fontSize = 40.sp, // Ajusta el tamaño de la fuente
                        textAlign = TextAlign.Center,
                        modifier = Modifier
                            .fillMaxWidth()
                    )
                },
                modifier = Modifier
                    .padding(top = 60.dp) // Agrega espacio en la parte superior de la TopAppBar
            )
        }
    ) {it->
        println(it)
        BodyContentHome(navController)
    }
}

@Composable
fun BodyContentHome(navController: NavController){
    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ){
        Button(
            onClick = {
                navController.navigate(
                    route = AppScreen.multasScreen.route
                )
            },
            modifier = Modifier
                .padding(16.dp) // Añade espacio alrededor del botón
                .height(60.dp)   // Ajusta la altura del botón
                .width(260.dp)  // Ajusta la anchura del botón
        ) {
            Text(
                text = "Registrar Multas",
                fontSize = 18.sp // Ajusta el tamaño de la fuente
            )
        }
        Button(
            onClick = {
                navController.navigate(route = AppScreen.solicitudScreen.route + "/" + "0")
            },
            modifier = Modifier
                .padding(26.dp) // Añade espacio alrededor del botón
                .height(60.dp)   // Ajusta la altura del botón
                .width(260.dp)  // Ajusta la anchura del botón
        ) {
            Text(
                text = "Ver Multas",
                fontSize = 18.sp // Ajusta el tamaño de la fuente
            )
        }
    }
}


@Preview
@Composable
fun HomeScreenPreview() {
    Avance_ProyectoTheme(darkTheme = false) {
        val navController = rememberNavController()
        HomeScreen(navController = navController)
    }
}