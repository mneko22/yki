package repositories

import "context"
import "log"
import "cloud.google.com/go/firestore"
import "yki/src/entities"

type FirestoreMotionRepository struct {
	projectID string
	ctx context.Context
	client *firestore.Client
}

func NewFirestoreMotionRepository(pi string) FirestoreMotionRepository{
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, pi)
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}
	return FirestoreMotionRepository{pi, ctx, client}
}

func (fmr FirestoreMotionRepository) Update(me entities.Motion) (entities.Motion, error) {
	c := fmr.client.Collection("Motion").Doc("Motion1")
	_, err := c.Set(fmr.ctx, map[string]interface{}{
		"motion": me.Status,
	})
	if err != nil {
		// TODO: Handle error.
		log.Print(err)
	}
	return me, nil
}

func (fmr FirestoreMotionRepository) Get() entities.Motion {
	c := fmr.client.Collection("Motion").Doc("Motion1")
	docsnap, err := c.Get(fmr.ctx)
	if err != nil {
		log.Print(err)
	}
	m := docsnap.Data()
	return entities.Motion{m["motion"].(bool)}
}
