package com.example.avance_proyecto.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.avance_proyecto.ui.view.HomeScreen
import com.example.avance_proyecto.ui.view.DetalleMultaScreen
import com.example.avance_proyecto.ui.view.SolicitudScreen
import com.example.avance_proyecto.ui.view.MultasScreen

@Composable
fun AppNavigation(){
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = AppScreen.homeScreen.route){
        composable(route = AppScreen.homeScreen.route){
            HomeScreen(navController)
        }
        composable(route = AppScreen.multasScreen.route ){
            MultasScreen(navController)
        }
        composable(route = AppScreen.solicitudScreen.route+"/{body}" ){
            val body = it.arguments?.getString("body") ?: "0"
            SolicitudScreen(navController,body)
        }
        composable(route = AppScreen.informationScreen.route ){
            DetalleMultaScreen(navController)
        }
    }
}