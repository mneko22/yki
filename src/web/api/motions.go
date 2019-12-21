package api

import "github.com/gin-gonic/gin"
import "net/http"

import "yki/src/gateways/controllers"
import "yki/src/gateways/repositories"

type Request struct {
	Motion bool `json:"motion"`
}

func Liten() {
	router := gin.Default()

	// Simple group: v1
	v1 := router.Group("/v1")
	{
		v1.POST("/motions", postMotions)
	}

	router.Run(":8080")
}

func postMotions(c *gin.Context) {
	immr := repositories.NewInMemoryMotionRepository()
	mc := controllers.NewMotionController(immr)
	req := load(c)
	m := mc.ConverToMotion(req.Motion)
	// m := mc.ConverToMotion(true)
	mc.Update(m)
	c.JSON(http.StatusOK, mc.Get())
}

func load(c *gin.Context) Request{
	var req Request
	c.BindJSON(&req)
	return req
}
