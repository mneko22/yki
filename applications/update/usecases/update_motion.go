package usecases

import "yki/src/entities"
import "yki/src/gateways/repositories"

func UpdateMotion(m entities.Motion, mr repositories.Motioner) (entities.Motion, error) {
	return mr.Update(m)
}
